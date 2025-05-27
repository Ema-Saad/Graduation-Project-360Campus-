from rest_framework.authtoken import views
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.urls import path
from .views import *
from .models import *
from .serializers import *

app_name = 'main'
urlpatterns = [
    path('api/auth/login', views.obtain_auth_token),
    path('api/role', role_view),
    path('api/courses', course_list, name='course_list'),
    path('api/registered_classrooms', registered_classroom_list, name='classroom_list'),
    path('api/colleges', \
         ListAPIView.as_view(queryset=College.objects.all(), serializer_class=CollegeSerializer), \
         name='college_list'),
    path('api/course/<int:pk>', \
         RetrieveAPIView.as_view(queryset=Course.objects.all(), serializer_class=CourseSerializer), \
         name='course_view'),
    path('api/course/<int:pk>/edit', course_edit, name='course_edit'),
    path('api/material/<int:pk>/', material_view, name='material_view'),
    path('api/material/<int:pk>/edit', material_create_modify, name='material_edit'),
    path('api/material/<int:pk>/delete', material_delete, name='material_delete'),
    path('api/course/<int:pk>/classroom', registered_classroom_view, name='classroom_view'),
    path('api/course/<int:pk>/classrooms', classroom_list, name='classroom_list'),
    path('api/course/<int:pk>/materials', material_list, name='material_list'),
    path('api/course/<int:pk>/material/add', material_create_modify, name='material_create'),
    path('api/course/<int:pk>/classroom/join', classroom_join, name='classroom_join'),
    path('api/course/<int:pk>/classroom/tasks', task_list, name='task_list'),
    path('api/course/<int:pk>/classroom/assignments', assignment_list, name='assignment_list'),
    path('api/course/<int:pk>/classroom/assignments/submitted', submitted_assignment_list, name='assignment_list'),
    path('api/course/<int:pk>/classroom/assignments/add', assignment_create, name='assginemnt_create'),

    #Event
    path('api/events', event_list, name='event_list'),
    path('api/events/registered', registered_event_list, name='registered_event_list'),
    path('api/event/<int:pk>/register', event_register, name='event_register'),
    #Graduation Project
    path('api/graduation-projects/',graduation_project_list, name='graduation_project_list'),
    path('api/graduation-project/<int:project_id>/', graduation_project_detail, name = 'graduation_project_detail'),
    path('api/assignment/<int:assignment_pk>', assignment_view, name='assignment_view'),
    path('api/assignment/<int:pk>/submission', assignment_submission_view, name='assignment_submission_view'),
    path('api/assignment/<int:pk>/submit/<str:filename>', assignment_submit, name='assignment_submit'),
    path('api/assignment/<int:pk>/unsubmit', assignment_unsubmit, name='assignment_unsubmit'),
]

