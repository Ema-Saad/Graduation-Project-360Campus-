from rest_framework.decorators import api_view
from django.urls import reverse

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

