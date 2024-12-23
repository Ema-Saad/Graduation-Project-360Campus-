from rest_framework.authtoken import views
from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('api/auth/login', views.obtain_auth_token),
    path('api/courses', course_list, name='course_list'),
    path('api/course/<int:course_pk>', course_view, name='course_view'),
    path('api/course/<int:course_pk>/classroom', classroom_view, name='classroom_view'),
    path('api/course/<int:course_pk>/materials', material_list, name='material_list'),
    path('api/course/<int:course_pk>/material/<int:material_pk>', material_view, name='material_view'),
]

