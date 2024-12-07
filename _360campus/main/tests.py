from django.test import TestCase, Client
from django.shortcuts import reverse
from django.http import request
from .models import *

class TestStudentAccessClassroom(TestCase):

    def setUp(self):
        student = Student.objects.create(first_name='John', last_name='Doe', email='email@domain.com', person_type='S')
        student.set_password('test')

        course = Course.objects.create(title='Course 1', description='Desc. 1')
        Course.objects.create(title='Course 2', description='Desc. 2')

        Enrollment.objects.create(student=student, course=course)
        classroom = Classroom.objects.create(course=course, title='Course 1 - 2020')
        classroom.students.add(student)
        classroom.save()

        self.client.login(email='email@domain.com', password='test')

    def test_access_to_registered_course(self):
        result = self.client.get(reverse('main:course_view', kwargs={'course_pk': 1}))
        self.assertEqual(200, result.status_code, 'failed to access a registered course')

    def test_access_to_nonregistered_course(self):
        result = self.client.get(reverse('main:course_view', kwargs={'course_pk': 2}))
        self.assertEqual(401, result.status_code, 'failed to deny access to unregistered course')

    def test_access_to_nonexistant_course(self):
        result = self.client.get(reverse('main:course_view', kwargs={'course_pk': 100}))
        self.assertEqual(404, result.status_code, 'failed to return error on nonexistant course')

class TestStudentAccessMaterials(TestCase):

    def setUp(self):
        student = Student.objects.create(first_name='John', last_name='Doe', email='john@example.com', person_type='S')
        student.set_password('test')
        course = Course.objects.create(title='Course 1')
        another = Course.objects.create(title='Course 2')
        Enrollment.objects.create(student=student, course=course)

        classroom = Classroom.objects.create(title='Course 1 - 2020', course=course)
        classroom.students.add(student)
        classroom.save()
        another_classroom = Classroom.objects.create(title='Course 2 - 2021', course=another)

        Material.objects.create(classroom=classroom, name='material')
        Material.objects.create(classroom=another_classroom, name='something else')
        self.client.login(email='john@example.com', password='test')

    def test_access_to_existing_material(self):
        result = self.client.get(reverse('main:material_view', kwargs={'course_pk': 1, 'material_pk': 1}))
        self.assertEqual(200, result.status_code, 'failed to access a material in classroom of a registered course')

    def test_access_to_nonexisting_material(self):
        result = self.client.get(reverse('main:material_view', kwargs={'course_pk': 1, 'material_pk': 10}))
        self.assertEqual(404, result.status_code)

    def test_access_to_existing_material_in_nonregistered_course(self):
        result = self.client.get(reverse('main:material_view', kwargs={'course_pk': 2, 'material_pk': 1}))
        self.assertEqual(401, result.status_code)

    def test_access_to_materials_in_nonexistant_course(self):
        result = self.client.get(reverse('main:material_view', kwargs={'course_pk': 10, 'material_pk': 10}))
        self.assertEqual(404, result.status_code)


