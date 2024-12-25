from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.urls import reverse
from .models import *
from .serializers import *

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

