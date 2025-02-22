from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import *
from .serializers import *
import datetime

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def event_list(req):
    limit = req.GET['limit'] if 'limit' in req.GET else 5
    events = Event.objects.all()[:limit]
    serializer = EventSerializer(events, many=True)

    return Response(serializer.data)

def course_list(req):
    return HttpResponseNotFound()

def course_view(req, course_pk):
    return HttpResponseNotFound()

def classroom_view(req, course_pk):
    return HttpResponseNotFound()

def material_list(req, course_pk):
    return HttpResponseNotFound()

def material_view(req, course_pk, material_pk):
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



