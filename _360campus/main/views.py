from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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

def classroom_view(req, course_pk):
    return HttpResponseNotFound()

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
def material_list(request, course_pk):
    materials = Material.objects.all()
    
    if course_pk:
        materials = materials.filter(classroom__course__pk=course_pk)
    
    college = request.query_params.get('college')
    if college:
        materials = materials.filter(classroom__course__college__iexact=college)
    
    year = request.query_params.get('year')
    if year:
        materials = materials.filter(classroom__course__year__iexact=year)
    
    semester = request.query_params.get('semester')
    if semester:
        materials = materials.filter(classroom__course__semester=semester)
    
    serializer = MaterialSerializer(materials, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def material_view(request, course_pk, material_pk):
    """
    Retrieve details for a specific material.
    It ensures the material belongs to the course with id course_pk.
    """
    material = get_object_or_404(Material, pk=material_pk, classroom__course__pk=course_pk)
    serializer = MaterialSerializer(material)
    return Response(serializer.data)




