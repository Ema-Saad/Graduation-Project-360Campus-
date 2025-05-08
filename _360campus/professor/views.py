from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage
import zipfile
import os
from django.conf import settings
from django.utils import timezone
from .models import *
from main.serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def material_list(req, pk):
    course = get_object_or_404(Course, pk=pk)
    try:
        professor = Professor.objects.get(id=req.user.id)
    except Professor.DoesNotExist:
        return Response({'detail': 'Professor profile not found.'}, status=status.HTTP_403_FORBIDDEN)

    materials = course.material_set.filter(created_by=professor)
    if not materials.exists():
        return Response({"message": "No materials found for this professor."}, status=404)
    serializer = MaterialSerializer(materials, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_material(request):
    professor = request.user
    if professor.person_type != 'P':
        return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    
    course_name = request.data.get('course_name')
    zip_file = request.FILES.get('file')

    if not course_name:
        return Response({'detail': 'Course name is required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not zip_file:
        return Response({'detail': 'No file uploaded.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not zip_file.name.endswith('.zip'):
        return Response({'detail': 'File must be a zip file.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        professor_instance = Professor.objects.get(id=professor.id)
    except Professor.DoesNotExist:
        return Response({'detail': 'Professor profile not found.'}, status=status.HTTP_400_BAD_REQUEST)

    course, created = Course.objects.get_or_create(
        title=course_name,
        prof=professor_instance,
        defaults={
            'college': professor_instance.faculty.college,
            'level': 1,
            'semester_kind': 'F'
        }
    )

    # Use MEDIA_ROOT for storage
    fs = FileSystemStorage(location=settings.MEDIA_ROOT)
    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

    try:
        file_path = fs.save(zip_file.name, zip_file)
        full_file_path = os.path.join(fs.location, file_path)
        print(f"Zip file saved to: {full_file_path}")
    except OSError as e:
        return Response({'detail': f'Failed to save file: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    try:
        with zipfile.ZipFile(full_file_path, 'r') as zip_ref:
            extract_path = os.path.join(settings.MEDIA_ROOT, course.title)
            os.makedirs(extract_path, exist_ok=True)
            zip_ref.extractall(extract_path)
            print(f"Extracted to: {extract_path}")

        for week_dir in os.listdir(extract_path):
            week_path = os.path.join(extract_path, week_dir)
            if os.path.isdir(week_path) and 'Week' in week_dir:  # Only process directories starting with 'Week'
                try:
                    week_number = int(''.join(filter(str.isdigit, week_dir)))
                    print(f"Parsed week_number from '{week_dir}': {week_number}")
                except ValueError:
                    week_number = 1
                    print(f"Failed to parse week from '{week_dir}', defaulting to {week_number}")
                for material_file in os.listdir(week_path):
                    material_full_path = os.path.join(week_path, material_file)
                    material_save_path = os.path.join(week_dir, material_file)  # Avoid nesting course title
                    with open(material_full_path, 'rb') as f:
                        material = Material(
                            course=course,
                            name=material_file,
                            week=week_number,
                            material_type=determine_material_type(material_file),
                            created_by=professor_instance
                        )
                        material.file.save(material_save_path, f)
                        print(f"Material saved: id={material.id}, week={material.week}, file={material.file.name}")
                    os.remove(material_full_path)

        os.remove(full_file_path)
        print(f"Deleted zip file: {full_file_path}")

        return Response({'detail': 'Materials uploaded successfully.'}, status=status.HTTP_201_CREATED)

    except zipfile.BadZipFile as e:
        os.remove(full_file_path) if os.path.exists(full_file_path) else None
        return Response({'detail': f'Invalid zip file: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    except OSError as e:
        os.remove(full_file_path) if os.path.exists(full_file_path) else None
        return Response({'detail': f'File system error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        os.remove(full_file_path) if os.path.exists(full_file_path) else None
        return Response({'detail': f'Unexpected error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def determine_material_type(file_name):
    if "lecture" in file_name.lower():
        return 'L'  # Lecture
    elif "tutorial" in file_name.lower():
        return 't'  # Tutorial
    elif "lab" in file_name.lower():
        return 'l'  # Lab
    else:
        return 'o'  # Other

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_material_page(request, pk):
    course = get_object_or_404(Course, pk=pk)
    try:
        professor = Professor.objects.get(id=request.user.id)
    except Professor.DoesNotExist:
        return Response({'detail': 'Professor profile not found.'}, status=status.HTTP_403_FORBIDDEN)

    if course.prof.id != professor.id:
        return Response({'detail': 'Unauthorized access.'}, status=status.HTTP_403_FORBIDDEN)

    materials = Material.objects.filter(course=course, created_by=professor).order_by('week')
    materials_by_week = {}
    for material in materials:
        week = material.week if material.week else 0
        if week not in materials_by_week:
            materials_by_week[week] = []
        material_data = {
            'id': material.id,
            'name': material.name,
            'material_type': material.material_type,
            'material_type_display': material.get_material_type_display(),
            'file_url': material.file.url if material.file else None,
        }
        materials_by_week[week].append(material_data)

    response_data = {
        'course': {
            'id': course.id,
            'title': course.title,
        },
        'materials_by_week': [
            {'week': week, 'materials': materials}
            for week, materials in materials_by_week.items()
        ]
    }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_new_week(request, pk):
    course = get_object_or_404(Course, pk=pk)
    try:
        professor = Professor.objects.get(id=request.user.id)
    except Professor.DoesNotExist:
        return Response({'detail': 'Professor profile not found.'}, status=status.HTTP_403_FORBIDDEN)

    if course.prof.id != professor.id:
        return Response({'detail': 'Unauthorized access.'}, status=status.HTTP_403_FORBIDDEN)

    week_number = request.data.get('week_number')
    files = request.FILES.getlist('files')

    if not week_number or not files:
        return Response({'detail': 'Week number and at least one file are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        week_number = int(week_number)
    except ValueError:
        return Response({'detail': 'Invalid week number.'}, status=status.HTTP_400_BAD_REQUEST)

    for file in files:
        material = Material(
            course=course,
            name=file.name,
            week=week_number,
            material_type=determine_material_type(file.name),
            created_by=professor
        )
        material.file.save(file.name, file)
        material.save()

    return Response({'detail': 'Materials added successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_course_materials(request, pk):
    course = get_object_or_404(Course, pk=pk)
    try:
        professor = Professor.objects.get(id=request.user.id)
    except Professor.DoesNotExist:
        return Response({'detail': 'Professor profile not found.'}, status=status.HTTP_403_FORBIDDEN)

    if course.prof.id != professor.id:
        return Response({'detail': 'Unauthorized access.'}, status=status.HTTP_403_FORBIDDEN)

    Material.objects.filter(course=course, created_by=professor).delete()
    return Response({'detail': 'All materials for the course have been removed.'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def class_list(request):
    """
    List all courses (classes) created by the logged-in professor.
    """
    try:
        professor = Professor.objects.get(id=request.user.id)
    except Professor.DoesNotExist:
        return Response({'detail': 'Professor profile not found.'}, status=status.HTTP_403_FORBIDDEN)

    courses = Course.objects.filter(prof=professor)
    response_data = [
        {
            'id': course.id,
            'title': course.title,
            'description': course.description,
            'level': course.level,
            'semester_kind': course.semester_kind,
        }
        for course in courses
    ]
    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def class_detail(request, pk):
    """
    Display the content of a specific class (course) organized by weeks.
    For each week, list material types with options to preview/delete or upload if none exist.
    """
    course = get_object_or_404(Course, pk=pk)
    try:
        professor = Professor.objects.get(id=request.user.id)
    except Professor.DoesNotExist:
        return Response({'detail': 'Professor profile not found.'}, status=status.HTTP_403_FORBIDDEN)

    if course.prof.id != professor.id:
        return Response({'detail': 'Unauthorized access.'}, status=status.HTTP_403_FORBIDDEN)

    # Define all possible material types
    MATERIAL_TYPES = {
        'L': 'Lecture',
        'l': 'Lab',
        't': 'Tutorial',
        'a': 'Assignment',
        's': 'Problem Sheet',
        'o': 'Other',
    }

    # Get all materials for the course
    materials = Material.objects.filter(course=course, created_by=professor).order_by('week')
    materials_by_week = {}

    # Group materials by week
    for material in materials:
        week = material.week if material.week else 0
        if week not in materials_by_week:
            materials_by_week[week] = {}

        # Initialize material types for this week if not already present
        for mat_type, mat_display in MATERIAL_TYPES.items():
            if mat_type not in materials_by_week[week]:
                materials_by_week[week][mat_type] = {
                    'type': mat_type,
                    'type_display': mat_display,
                    'materials': [],
                    'has_materials': False,
                }

        # Add the material to its type
        material_data = {
            'id': material.id,
            'name': material.name,
            'file_url': material.file.url if material.file else None,
        }
        materials_by_week[week][material.material_type]['materials'].append(material_data)
        materials_by_week[week][material.material_type]['has_materials'] = True

    # Ensure all weeks have all material types, even if empty
    for week in materials_by_week:
        for mat_type, mat_display in MATERIAL_TYPES.items():
            if mat_type not in materials_by_week[week]:
                materials_by_week[week][mat_type] = {
                    'type': mat_type,
                    'type_display': mat_display,
                    'materials': [],
                    'has_materials': False,
                }

    # Format response
    response_data = {
        'course': {
            'id': course.id,
            'title': course.title,
            'description': course.description,
        },
        'materials_by_week': [
            {
                'week': week,
                'material_types': [
                    mat_data for mat_type, mat_data in week_materials.items()
                ]
            }
            for week, week_materials in materials_by_week.items()
        ]
    }
    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_material(request, pk, material_id):
    """
    Delete a specific material from a course.
    """
    course = get_object_or_404(Course, pk=pk)
    try:
        professor = Professor.objects.get(id=request.user.id)
    except Professor.DoesNotExist:
        return Response({'detail': 'Professor profile not found.'}, status=status.HTTP_403_FORBIDDEN)

    if course.prof.id != professor.id:
        return Response({'detail': 'Unauthorized access.'}, status=status.HTTP_403_FORBIDDEN)

    material = get_object_or_404(Material, id=material_id, course=course, created_by=professor)
    material.delete()
    return Response({'detail': 'Material deleted successfully.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_material_by_type(request, pk):
    """
    Upload a material for a specific material type in a specific week.
    """
    course = get_object_or_404(Course, pk=pk)
    try:
        professor = Professor.objects.get(id=request.user.id)
    except Professor.DoesNotExist:
        return Response({'detail': 'Professor profile not found.'}, status=status.HTTP_403_FORBIDDEN)

    if course.prof.id != professor.id:
        return Response({'detail': 'Unauthorized access.'}, status=status.HTTP_403_FORBIDDEN)

    week_number = request.data.get('week_number')
    material_type = request.data.get('material_type')
    file = request.FILES.get('file')

    if not all([week_number, material_type, file]):
        return Response({'detail': 'Week number, material type, and file are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        week_number = int(week_number)
    except ValueError:
        return Response({'detail': 'Invalid week number.'}, status=status.HTTP_400_BAD_REQUEST)

    # Validate material type
    valid_material_types = [choice[0] for choice in Material.MATERIAL_TYPE]
    if material_type not in valid_material_types:
        return Response({'detail': 'Invalid material type.'}, status=status.HTTP_400_BAD_REQUEST)

    material = Material(
        course=course,
        name=file.name,
        week=week_number,
        material_type=material_type,
        created_by=professor
    )
    material_save_path = os.path.join(f'Week {week_number}', file.name)
    material.file.save(material_save_path, file)
    material.save()

    return Response({'detail': 'Material uploaded successfully.'}, status=status.HTTP_201_CREATED)

# New Chat Views

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_chatroom(request, pk):
    """
    Retrieve the chatroom for a course.
    """
    course = get_object_or_404(Course, pk=pk)
    chatroom = get_object_or_404(Chatroom, course=course)

    # Check if the user is a participant (professor, student, or TA)
    try:
        classroom = Classroom.objects.get(course=course)
    except Classroom.DoesNotExist:
        return Response({'detail': 'Classroom not found for this course.'}, status=status.HTTP_404_NOT_FOUND)

    user = request.user
    is_participant = (
        (user.person_type == 'P' and classroom.instructor.id == user.id) or
        (user.person_type == 'S' and classroom.students.filter(id=user.id).exists()) or
        (user.person_type == 'T' and classroom.teaching_assistants.filter(id=user.id).exists())
    )

    if not is_participant:
        return Response({'detail': 'You are not a participant in this course.'}, status=status.HTTP_403_FORBIDDEN)

    return Response({
        'chatroom_id': chatroom.id,
        'title': chatroom.title,
        'course_id': course.id,
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_participants(request, pk):
    """
    List all participants in the course (professor, TAs, students).
    """
    course = get_object_or_404(Course, pk=pk)
    try:
        classroom = Classroom.objects.get(course=course)
    except Classroom.DoesNotExist:
        return Response({'detail': 'Classroom not found for this course.'}, status=status.HTTP_404_NOT_FOUND)

    user = request.user
    is_participant = (
        (user.person_type == 'P' and classroom.instructor.id == user.id) or
        (user.person_type == 'S' and classroom.students.filter(id=user.id).exists()) or
        (user.person_type == 'T' and classroom.teaching_assistants.filter(id=user.id).exists())
    )

    if not is_participant:
        return Response({'detail': 'You are not a participant in this course.'}, status=status.HTTP_403_FORBIDDEN)

    participants = []
    # Add professor
    participants.append({
        'id': classroom.instructor.id,
        'username': classroom.instructor.username,
        'role': 'Professor',
    })

    # Add TAs
    for ta in classroom.teaching_assistants.all():
        participants.append({
            'id': ta.id,
            'username': ta.username,
            'role': 'Teaching Assistant',
        })

    # Add students
    for student in classroom.students.all():
        participants.append({
            'id': student.id,
            'username': student.username,
            'role': 'Student',
        })

    return Response(participants, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def chat_messages(request, pk):
    """
    GET: Retrieve all messages in the course's chatroom.
    POST: Send a new message to the chatroom.
    """
    course = get_object_or_404(Course, pk=pk)
    chatroom = get_object_or_404(Chatroom, course=course)

    try:
        classroom = Classroom.objects.get(course=course)
    except Classroom.DoesNotExist:
        return Response({'detail': 'Classroom not found for this course.'}, status=status.HTTP_404_NOT_FOUND)

    user = request.user
    is_participant = (
        (user.person_type == 'P' and classroom.instructor.id == user.id) or
        (user.person_type == 'S' and classroom.students.filter(id=user.id).exists()) or
        (user.person_type == 'T' and classroom.teaching_assistants.filter(id=user.id).exists())
    )

    if not is_participant:
        return Response({'detail': 'You are not a participant in this course.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        messages = chatroom.messages.all().order_by('sent_at')
        response_data = [
            {
                'id': message.id,
                'sender': {
                    'id': message.sender.id,
                    'username': message.sender.username,
                    'role': message.sender.person_type,
                },
                'content': message.content,
                'sent_at': message.sent_at,
            }
            for message in messages
        ]
        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        content = request.data.get('content')
        if not content:
            return Response({'detail': 'Message content is required.'}, status=status.HTTP_400_BAD_REQUEST)

        message = Message(
            chatroom=chatroom,
            sender=user,
            content=content
        )
        message.save()
        return Response({
            'id': message.id,
            'sender': {
                'id': message.sender.id,
                'username': message.sender.username,
                'role': message.sender.person_type,
            },
            'content': message.content,
            'sent_at': message.sent_at,
        }, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_events(request):
    """
    Retrieve a list of upcoming events.
    """
    today = timezone.now()
    events = Event.objects.filter(date__gte=today).order_by('date')
    response_data = [
        {
            'id': event.id,
            'title': event.title,
            'description': event.description,
            'date': event.date,
            'is_registered': EventRegistration.objects.filter(person=request.user, event=event).exists()
        }
        for event in events
    ]
    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def event_register(req, pk):
    """
    Register a person (student, professor, TA, or Admin) for an event.
    """
    evt = get_object_or_404(Event, pk=pk)

    # Check if the user is already registered
    if EventRegistration.objects.filter(person=req.user, event=evt).exists():
        return Response({'detail': 'Already registered for this event.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    today = timezone.now()
    if today > evt.date:
        return Response({'detail': 'Event date has passed.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # Create registration for the person
    EventRegistration.objects.create(event=evt, person=req.user)

    return Response({'detail': 'Successfully registered for the event.'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_projects(request):
    """
    List all graduation projects supervised by the authenticated professor.
    """
    projects = GraduationProject.objects.filter(supervisor=request.user)
    data = [
        {
            'id': project.id,
            'name': project.name,
            'year': project.year,
            'faculty': project.faculty.name,
            'description': project.description,
            'rate': float(project.rate),  # Represents the grade (0.00 to 4.00)
        }
        for project in projects
    ]
    return Response({'projects': data, 'empty': len(data) == 0}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_project(request):
    """
    Add a new graduation project for the authenticated professor.
    """
    name = request.data.get('name')
    year = request.data.get('year')
    faculty_code = request.data.get('faculty')
    description = request.data.get('description')
    rate = request.data.get('rate')

    if not all([name, year, faculty_code, description]):
        return Response({'detail': 'All fields except rate are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        faculty = Faculty.objects.get(code=faculty_code)
    except Faculty.DoesNotExist:
        return Response({'detail': 'Invalid faculty code.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        year_value = int(year)  # Explicitly convert year to integer
    except (ValueError, TypeError):
        return Response({'detail': 'Year must be a valid integer.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        rate_value = float(rate) if rate else 0.00
        if rate_value < 0.00 or rate_value > 4.00:
            return Response({'detail': 'Rate must be between 0.00 and 4.00.'}, status=status.HTTP_400_BAD_REQUEST)
    except (ValueError, TypeError):
        return Response({'detail': 'Rate must be a valid number.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        project = GraduationProject.objects.create(
            name=name,
            year=year_value,
            faculty=faculty,
            description=description,
            supervisor=request.user,
            rate=rate_value
        )
        return Response({'detail': 'Project added successfully.', 'id': project.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'detail': f'Failed to create project: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_project(request, pk):
    """
    Delete a graduation project supervised by the authenticated professor.
    """
    project = get_object_or_404(GraduationProject, pk=pk, supervisor=request.user)
    project.delete()
    return Response({'detail': 'Project deleted successfully.'}, status=status.HTTP_200_OK)