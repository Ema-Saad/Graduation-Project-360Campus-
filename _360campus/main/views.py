from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import *
from .serializers import *
import datetime
from django.http import HttpResponseNotFound


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def event_list(req):
    limit = req.GET['limit'] if 'limit' in req.GET else 5
    events = Event.objects.all()[:limit]
    serializer = EventSerializer(events, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def registered_event_list(req):
    registered_events = EventRegistration.objects.filter(student=req.user.student).values("event")

    return Response(registered_events)

def course_list(req):
    return HttpResponseNotFound()

def course_view(req, course_pk):
    return HttpResponseNotFound()

@api_view(['GET'])
def classroom_view(req, course_pk):
    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def event_register(req, pk):
    evt = get_object_or_404(Event, pk=pk)

    # TODO: This looks weird
    try:
        EventRegistration.objects.get(student=req.user.student, event=evt)
        return Response(status=422)
    except EventRegistration.DoesNotExist:
        pass

    today = datetime.datetime.now(tz=datetime.timezone.utc)
    if today > evt.date:
        return Response(status=422)

    # TODO: Ensure that req.user is a student
    EventRegistration.objects.create(event=evt, student=req.user.student) 

    return Response(status=200)

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
