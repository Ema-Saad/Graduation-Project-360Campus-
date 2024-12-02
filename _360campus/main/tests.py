from django.test import TestCase, Client
from django.shortcuts import reverse
from django.http import request
from .models import *

class TestStudentAccessClassroom(TestCase):

    def setUp(self):
        student = Student.objects.create(name='Student 1')

        course = Course.objects.create(name='Course 1', description='Desc. 1')
        Course.objects.create(name='Course 2', description='Desc. 2')

        Enrollment.objects.create(student, course)

        self.client.login(student)

    def test_access_to_registered_course(self):
        result = self.client.get(reverse('course_view', kwargs={'course_pk': 1}))
        self.assertEqual(200, result.status_code, 'failed to access a registered course')

    def test_access_to_nonregistered_course(self):
        result = self.client.get(reverse('course_view', kwargs={'course_pk': 2}))
        self.assertEqual(401, result.status_code, 'failed to deny access to unregistered course')

    def test_access_to_nonexistant_course(self):
        result = self.client.get(reverse('course_view', kwargs={'course_pk': 100}))
        self.assertEqual(404, result.status_code, 'failed to return error on nonexistant course')

class TestStudentAccessMaterials(TestCase):

    def setUp(self):
        pass

    def test_access_to_existing_material(self):
        pass

    def test_access_to_nonexisting_material(self):
        pass

    def test_access_to_existing_material_in_nonregistered_course(self):
        pass

    def test_access_to_nonexisting_material_in_nonregistered_course(self):
        pass

    def test_access_to_materials_in_nonexistant_course(self):
        pass


