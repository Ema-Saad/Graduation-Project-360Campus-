from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from professor.views import *

app_name = 'professor'

urlpatterns = [
    path('api/auth/login/', obtain_auth_token, name='auth_login'),  # Auth login API  
    path('api/courses/<int:pk>/materials/', material_list, name='material_list'),  # Materials for a specific course
    path('api/upload-material/', upload_material, name='upload_material'),  # Upload materials for a course
    path('api/courses/<int:pk>/material-page/', course_material_page, name='course_material'),  # Fetch course materials by week
    path('api/courses/<int:pk>/add-week/', add_new_week, name='add_new_week'),  # Add materials for a new week
    path('api/courses/<int:pk>/remove-materials/', remove_course_materials, name='remove_course_materials'),  # Remove all materials for a course
    #  URLs for class section
    path('classes/',class_list, name='class_list'),
    path('class/<int:pk>/',class_detail, name='class_detail'),
    path('class/<int:pk>/material/<int:material_id>/delete/',delete_material, name='delete_material'),
    path('class/<int:pk>/upload-material/',upload_material_by_type, name='upload_material_by_type'),
    #  Chat URLs
    path('class/<int:pk>/chatroom/', get_chatroom, name='get_chatroom'),
    path('class/<int:pk>/participants/', get_participants, name='get_participants'),
    path('class/<int:pk>/messages/',chat_messages, name='chat_messages'),
    # New Event URLs
    path('events/', list_events, name='list_events'),
    path('events/<int:pk>/register/', event_register, name='event_register'),
    
    
]