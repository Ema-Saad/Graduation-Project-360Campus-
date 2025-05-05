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
]