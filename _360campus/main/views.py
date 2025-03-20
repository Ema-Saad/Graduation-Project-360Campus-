from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import reverse
from .models import *
from .serializers import *
import datetime
from django.http import HttpResponseNotFound


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def event_list(req):
    limit = req.query_params['limit'] if 'limit' in req.query_params else 5
    events = Event.objects.all()[:limit]
    serializer = EventSerializer(events, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def registered_event_list(req):
    registered_events = EventRegistration.objects.filter(student=req.user.student).values("event")

    return Response(registered_events)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_list(req):
    options = {}
    if 'college' in req.query_params:
        options['college'] = req.query_params['college']

    if 'level' in req.query_params:
        options['level'] = req.query_params['level']

    if 'semester' in req.query_params:
        options['semester_kind'] = req.query_params['semester_kind']

    if 'search_query' in req.query_params:
        options['title__icontains'] = req.query_params['search_query']
        options['description__icontains'] = req.query_params['search_query']

    courses = get_list_or_404(Course, **options)
    serializer = CourseSerializer(courses, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def registered_classroom_view(req, course_pk):
    current_semester = Semester.objects.last()
    course = get_object_or_404(Course, pk=course_pk)

    if not Enrollment.objects.filter(classroom__semester=current_semester, \
                                     classroom__course=course, \
                                     student=req.user.student).exists():
        return Response(status=status.HTTP_403_FORBIDDEN)

    classroom = Classroom.objects.get(course=course, \
                                      semester=current_semester)
    serializer = ClassroomSerializer(classroom)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def registered_classroom_list(req):
    current_semester = Semester.objects.last()
    classrooms = Classroom.objects.filter(enrollment__student=req.user.student, \
                                          semester=current_semester)
    serializer = ClassroomSerializer(classrooms, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def classroom_list(req, course_pk):
    current_semester = Semester.objects.last()
    course = get_object_or_404(Course, pk=course_pk)
    classrooms = get_list_or_404(Classroom, semester=current_semester, \
                                 course=course)
    serializer = ClassroomSerializer(classrooms, many=True)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def classroom_join(req, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    if Enrollment.objects.filter(student=req.user.student, \
                                 classroom=classroom).exists():
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    Enrollment.objects.create(student=req.user.student, classroom=classroom)
    return Response(data={}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def event_register(req, pk):
    evt = get_object_or_404(Event, pk=pk)

    if EventRegistration.objects.filter(student=req.user.student, event=evt).exists():
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    today = datetime.datetime.now(tz=datetime.timezone.utc)
    if today > evt.date:
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # TODO: Ensure that req.user is a student
    EventRegistration.objects.create(event=evt, student=req.user.student)

    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def material_list(request):
    """
    Returns a list of all courses that have at least one material available on the website.
    Supports optional filtering by college, year, and semester via query parameters.
    For example:
      ?college=Engineering&year=First%20Year&semester=1
    """
    # Start with courses that have at least one material.
    courses = Course.objects.filter(materials__isnull=False).distinct()
    
    # Apply optional filters based on query parameters.
    college = request.query_params.get('college')
    if college:
        courses = courses.filter(college__iexact=college)
    
    year = request.query_params.get('year')
    if year:
        courses = courses.filter(year__iexact=year)
    
    semester = request.query_params.get('semester')
    if semester:
        courses = courses.filter(semester=semester)
    
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def course_materials_by_week(request, course_pk):
    """
    For the specified course, return a list of distinct weeks for which materials exist
    """
    # Using the direct relation from Material to Course.
    materials = Material.objects.filter(course__pk=course_pk)
    weeks = materials.values_list('week', flat=True).distinct().order_by('week')
    weeks = [w for w in weeks if w is not None]  # Exclude any materials without a week set.
    return Response([{"week": w} for w in weeks])

@api_view(['GET'])
def materials_for_week(request, course_pk, week):
    """
    Returns all materials for the specified course and week.
    """
    materials = Material.objects.filter(course__pk=course_pk, week=week)
    serializer = MaterialSerializer(materials, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def material_view(request, course_pk, week, material_pk):
    """
    Retrieves details for a specific material that belongs to the given course and week.
    Includes a download URL for the file.
    """
    material = get_object_or_404(Material, pk=material_pk, course__pk=course_pk, week=week)
    serializer = MaterialSerializer(material)
    data = serializer.data
    data['download_url'] = request.build_absolute_uri(material.file.url)
    return Response(data)

@api_view(['GET'])
def graduation_project_list(request):
    """
    Returns a list of all graduation projects sorted by rating (highest first).
    Supports optional filtering by:
      - faculty 
      - year 
    """
    projects = GraduationProject.objects.all().order_by('-rate')
    faculty = request.query_params.get('faculty')
    if faculty:
        projects = projects.filter(faculty__iexact=faculty)  # ✅ Case-insensitive

    year = request.query_params.get('year')
    if year:
        projects = projects.filter(year=year)

    serializer = GraduationProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def graduation_project_detail(request, project_id):
    """
    Retrieves details of a specific graduation project.
    """
    project = get_object_or_404(GraduationProject, id=project_id)
    serializer = GraduationProjectSerializer(project)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def assignment_list(req, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)

    if req.user.student not in classroom.students.all():
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    assignments = classroom.assignment_set.all()
    serializer = AssignmentSerializer(assignments, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def submitted_assignment_list(req, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)

    if req.user.student not in classroom.students.all():
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    submitted_assignments = AssignmentSubmission.objects.filter(student=req.user.student, \
                                                                assignment__classroom=classroom) \
                                                        .values('assignment')
    submitted_assignments = get_list_or_404(Assignment, pk__in=submitted_assignments)
    serializer = AssignmentSerializer(submitted_assignments, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def assignment_view(req, course_pk, assignment_pk):
    assignment = get_object_or_404(Assignment, \
                                   classroom__course__pk=course_pk, pk=assignment_pk)

    serializer = AssignmentSerializer(assignment)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assignment_submit(req, course_pk, assignment_pk):
    pass

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assignment_comment(req, course_pk, assignment_pk):
    pass

