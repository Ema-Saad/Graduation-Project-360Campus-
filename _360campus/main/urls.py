from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('student', student_home, name='student_home'),
    path('courses', course_list, name='course_list'),
    path('student/login', student_login, name='student_login'),
    path('student/logout', student_logout, name='student_logout'),
    path('course/<int:course_pk>', course_view, name='course_view'),
    path('course/<int:course_pk>/classroom', classroom_view, name='classroom_view'),
    path('course/<int:course_pk>/materials', material_list, name='material_list'),
    path('course/<int:course_pk>/material/<int:material_pk>', material_view, name='material_view'),
]

