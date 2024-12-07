from django.shortcuts import render
from django.http.response import HttpResponseNotFound

def student_login(req):
    return HttpResonseNotFound()

def student_logout(req):
    return HttpResponseNotFound()

def student_home(req):
    return HttpResponseNotFound()

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

