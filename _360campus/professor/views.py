from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage
import zipfile
import os
from django.conf import settings
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