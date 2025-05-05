from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
from django.utils.crypto import get_random_string
import zipfile
import os
from io import BytesIO
from django.conf import settings
import shutil

class UploadMaterialTestCase(APITestCase):

    def setUp(self):
        self.college, _ = College.objects.get_or_create(
            code='csit',
            defaults={
                'name': 'College of Science and Information Technology',
                'description': 'CSIT description'
            }
        )

        self.faculty, _ = Faculty.objects.get_or_create(
            code='ENG',
            defaults={
                'name': 'Engineering',
                'college': self.college,
                'description': 'Engineering faculty'
            }
        )

        random_suffix = get_random_string(length=5)
        self.user = Professor.objects.create(
            username=f'professor{random_suffix}',
            email=f'professor{random_suffix}@example.com',
            person_type='P',
            faculty=self.faculty
        )

        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        self.course = Course.objects.create(
            title='Test Course',
            description='Test course description',
            college=self.college,
            level=1,
            semester_kind='F',
            prof=self.user
        )

        self.upload_url = reverse('professor:upload_material')
        self.material_page_url = reverse('professor:course_material', kwargs={'pk': self.course.pk})
        self.add_week_url = reverse('professor:add_new_week', kwargs={'pk': self.course.pk})
        self.remove_materials_url = reverse('professor:remove_course_materials', kwargs={'pk': self.course.pk})

    def tearDown(self):
        Material.objects.all().delete()
        Course.objects.all().delete()
        Professor.objects.all().delete()
        get_user_model().objects.all().delete()
        Faculty.objects.all().delete()
        College.objects.all().delete()
        # Clean up uploaded files
        shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'Test Course'), ignore_errors=True)

    def create_test_zip(self, files):
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for file_name, content in files.items():
                zip_file.writestr(file_name, content)
        zip_buffer.seek(0)
        return SimpleUploadedFile(
            'test_material.zip',
            zip_buffer.read(),
            content_type='application/zip'
        )

    def test_upload_material_successfully(self):
        zip_file = self.create_test_zip({
            'Week 1/lecture.pdf': b'Dummy lecture content'
        })
        response = self.client.post(self.upload_url, {
            'course_name': self.course.title,
            'file': zip_file
        }, format='multipart')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['detail'], 'Materials uploaded successfully.')
        
        # Debug: Check all materials to see what was saved
        materials = Material.objects.filter(course=self.course, week=1)
        for material in materials:
            print(f"Found material: id={material.id}, name={material.name}, file={material.file.name}, course={material.course.title}, week={material.week}, created_by={material.created_by.id}")
        
        print(f"Expected course: {self.course.id}, user: {self.user.id}")
        material_exists = Material.objects.filter(
            course=self.course,
            name='lecture.pdf',
            week=1,
            created_by=self.user
        ).exists()
        self.assertTrue(material_exists, "Material not found in the database.")
        
        material = Material.objects.get(course=self.course, name='lecture.pdf')
        self.assertEqual(material.course, self.course)
        self.assertEqual(material.material_type, 'L')
        self.assertEqual(material.created_by, self.user)

    def test_upload_invalid_file_type(self):
        pdf_file = SimpleUploadedFile(
            'test_material.pdf',
            b"Dummy PDF content",
            content_type='application/pdf'
        )
        response = self.client.post(self.upload_url, {
            'course_name': self.course.title,
            'file': pdf_file
        }, format='multipart')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'File must be a zip file.')

    def test_upload_missing_file(self):
        response = self.client.post(self.upload_url, {
            'course_name': self.course.title
        }, format='multipart')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'No file uploaded.')

    def test_upload_without_login(self):
        self.client.credentials()
        zip_file = self.create_test_zip({
            'Week 1/lecture.pdf': b'Dummy lecture content'
        })
        response = self.client.post(self.upload_url, {
            'course_name': self.course.title,
            'file': zip_file
        }, format='multipart')
        self.assertEqual(response.status_code, 401)

    def test_course_material_page_success(self):
        zip_file = self.create_test_zip({
            'Week 1/lecture.pdf': b'Dummy lecture content'
        })
        self.client.post(self.upload_url, {
            'course_name': self.course.title,
            'file': zip_file
        }, format='multipart')

        response = self.client.get(self.material_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('course', response.data)
        self.assertIn('materials_by_week', response.data)
        self.assertEqual(response.data['course']['title'], 'Test Course')
        self.assertEqual(len(response.data['materials_by_week']), 1)
        self.assertEqual(response.data['materials_by_week'][0]['week'], 1)
        self.assertEqual(len(response.data['materials_by_week'][0]['materials']), 1)
        self.assertEqual(response.data['materials_by_week'][0]['materials'][0]['name'], 'lecture.pdf')

    def test_course_material_page_unauthorized(self):
        self.client.credentials()
        response = self.client.get(self.material_page_url)
        self.assertEqual(response.status_code, 401)

    def test_add_new_week_success(self):
        lecture_file = SimpleUploadedFile('lecture.pdf', b'Dummy lecture content', content_type='application/pdf')
        lab_file = SimpleUploadedFile('lab.pdf', b'Dummy lab content', content_type='application/pdf')
        data = {
            'week_number': '2',
            'files': [lecture_file, lab_file]
        }
        response = self.client.post(self.add_week_url, data, format='multipart')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['detail'], 'Materials added successfully.')

        materials = Material.objects.filter(course=self.course, week=2)
        self.assertEqual(materials.count(), 2)
        self.assertIn('lecture.pdf', [m.name for m in materials])
        self.assertIn('lab.pdf', [m.name for m in materials])

    def test_add_new_week_missing_data(self):
        response = self.client.post(self.add_week_url, {}, format='multipart')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Week number and at least one file are required.')

    def test_add_new_week_invalid_week(self):
        data = {
            'week_number': 'invalid',
            'files': [SimpleUploadedFile('lecture.pdf', b'Dummy lecture content', content_type='application/pdf')]
        }
        response = self.client.post(self.add_week_url, data, format='multipart')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Invalid week number.')

    def test_add_new_week_unauthorized(self):
        self.client.credentials()
        data = {
            'week_number': '2',
            'files': [SimpleUploadedFile('lecture.pdf', b'Dummy lecture content', content_type='application/pdf')]
        }
        response = self.client.post(self.add_week_url, data, format='multipart')
        self.assertEqual(response.status_code, 401)

    def test_remove_course_materials_success(self):
        zip_file = self.create_test_zip({
            'Week 1/lecture.pdf': b'Dummy lecture content'
        })
        self.client.post(self.upload_url, {
            'course_name': self.course.title,
            'file': zip_file
        }, format='multipart')

        response = self.client.delete(self.remove_materials_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['detail'], 'All materials for the course have been removed.')
        self.assertEqual(Material.objects.filter(course=self.course).count(), 0)

    def test_remove_course_materials_unauthorized(self):
        self.client.credentials()
        response = self.client.delete(self.remove_materials_url)
        self.assertEqual(response.status_code, 401)