from rest_framework.authtoken import views
from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('api/auth/login', views.obtain_auth_token),
    path('api/courses', course_list, name='course_list'),
    path('api/course/<int:course_pk>', course_view, name='course_view'),
    path('api/course/<int:course_pk>/classroom', classroom_view, name='classroom_view'),
    # Materials endpoints (for courses that have materials)
    path('api/materials', material_list, name='material_list'),
    path('api/course/<int:course_pk>/materials/weeks', course_materials_by_week, name='course_materials_by_week'),
    path('api/course/<int:course_pk>/materials/week/<int:week>', materials_for_week, name='materials_for_week'),
    #material itself "files or content"
    path('api/course/<int:course_pk>/material/<int:week>/<int:material_pk>', material_view, name='material_view'),
    #Event
    path('api/events', event_list, name='event_list'),
    path('api/events/registered', registered_event_list, name='registered_event_list'),
    path('api/event/<int:pk>/register', event_register, name='event_register'),
    #Graduation Project
    path('api/graduation-projects/',graduation_project_list, name='graduation_project_list'),
    path('api/graduation-project/<int:project_id>/', graduation_project_detail, name = 'graduation_project_detail')
    

]

