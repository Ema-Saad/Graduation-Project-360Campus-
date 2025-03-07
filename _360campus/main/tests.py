from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase, Client
from django.shortcuts import reverse
from django.http import request
from .models import *
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()
"""class TestStudentAccessClassroom(TestCase):

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


class TestStudentEventRegistration(APITestCase):

    def setUp(self):
        student = Student.objects.create(first_name='John',
                                         last_name='Dow',
                                         email='test@example.com',
                                         person_type='S')
        token = Token.objects.create(user=student)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        import datetime

        evt = Event.objects.create(title='event enrolled',
                                   date=datetime.date.today() + datetime.timedelta(weeks=2))

        Event.objects.create(title='event',
                             date=datetime.date.today() + datetime.timedelta(weeks=3))

        Event.objects.create(title='event passed',
                             date=datetime.date.today() + datetime.timedelta(days=-2))

        Event.objects.create(title='event today', date=datetime.date.today())

        EventRegistration.objects.create(event=evt, student=student)

    def test_enroll_in_event(self):
        evt = Event.objects.get(title='event')
        response = self.client.post(reverse('main:event_register', args=[evt.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_enroll_in_enrolled_event(self):
        evt = Event.objects.get(title='event enrolled')
        response = self.client.post(reverse('main:event_register', args=[evt.pk]))
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY) # TODO: validate this choice of status code

    def test_enroll_in_expired_event(self):
        evt = Event.objects.get(title='event passed')
        response = self.client.post(reverse('main:event_register', args=[evt.pk]))
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY) # TODO: validate this choice of status code

    def test_enroll_in_nonexistent_event(self):
        response = self.client.post(reverse('main:event_register', args=[100]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_enroll_in_event_happening_today(self):
        evt = Event.objects.get(title='event today')
        response = self.client.post(reverse('main:event_register', args=[evt.pk]))
        # FIXME: what should happen here ???
        
        
class TestMaterialsSection(APITestCase):
    def setUp(self):
        # Create a test student (and log them in)
        self.student = Student.objects.create_user(
            username='testuser', password='testpassword', person_type='S'
        )
        self.client.login(username='testuser', password='testpassword')

        # Create an admin for course management
        self.admin = Admin.objects.create_user(
            username='adminuser', password='adminpassword', person_type='A'
        )

        # Create two courses with filtering attributes (college, year, semester)
        self.course1 = Course.objects.create(
            title='Software Engineering', admin=self.admin,
            college='Engineering', year='First Year', semester=1
        )
        self.course2 = Course.objects.create(
            title='Medical Biology', admin=self.admin,
            college='Medicine', year='Second Year', semester=2
        )

        # Enroll student in course1 only (if needed)
        Enrollment.objects.create(student=self.student, course=self.course1)

        # Create classrooms for each course
        self.classroom1 = Classroom.objects.create(title='Software Engineering - 2024', course=self.course1)
        self.classroom2 = Classroom.objects.create(title='Medical Biology - 2024', course=self.course2)

        # Create materials for each classroom; **pass the direct course relationship**
        self.material1 = Material.objects.create(
            course=self.course1,                   # Added direct course reference
            classroom=self.classroom1,
            name='Material 1',
            file=SimpleUploadedFile("material1.pdf", b"Dummy content")
        )
        self.material2 = Material.objects.create(
            course=self.course2,                   # Added direct course reference
            classroom=self.classroom2,
            name='Material 2',
            file=SimpleUploadedFile("material2.pdf", b"Dummy content")
        )

    def test_material_list_returns_all_materials(self):
        url = reverse('main:material_list', kwargs={'course_pk': self.course1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_material_view_returns_correct_material(self):
        url = reverse('main:material_view', kwargs={'course_pk': self.course1.pk, 'material_pk': self.material1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'Material 1')

    def test_material_view_non_existent_material(self):
        url = reverse('main:material_view', kwargs={'course_pk': self.course1.pk, 'material_pk': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        """
        
class GraduationProjectTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create test graduation projects
        self.project1 = GraduationProject.objects.create(
            name='AI-Powered Diagnosis',
            faculty='Engineering',
            year=2023,
            description='A machine learning model for medical diagnosis.',
            rate=4.8,
        )

        self.project2 = GraduationProject.objects.create(
            name='Smart Traffic Management',
            faculty='Computer Science',
            year=2024,
            description='AI-based system to optimize traffic flow.',
            rate=4.5,
        )

    def test_graduation_project_list_view(self):
        url = reverse('main:graduation_project_list') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'AI-Powered Diagnosis')
        self.assertContains(response, 'Smart Traffic Management')

    def test_filter_by_faculty(self):
        url = reverse('main:graduation_project_list') + '?faculty=Engineering' 
        response = self.client.get(url)
        self.assertContains(response, 'AI-Powered Diagnosis')
        self.assertNotContains(response, 'Smart Traffic Management')

    def test_filter_by_year(self):
        url = reverse('main:graduation_project_list') + '?year=2024' 
        response = self.client.get(url)
        self.assertContains(response, 'Smart Traffic Management')
        self.assertNotContains(response, 'AI-Powered Diagnosis')

    def test_graduation_project_detail_view(self):
        url = reverse('main:graduation_project_detail', args=[self.project1.id])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'AI-Powered Diagnosis')
        self.assertContains(response, 'A machine learning model for medical diagnosis.')