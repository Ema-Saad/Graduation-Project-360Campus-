from django.test import TestCase, Client
from django.shortcuts import reverse
from .models import *

class TestStudentAccessClassroom(TestCase):

    def setUp(self):
        pass

    def test_access_to_registered_course(self):
        pass

    def test_access_to_nonregistered_course(self):
        pass

    def test_access_to_nonexistant_course(self):
        pass

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


