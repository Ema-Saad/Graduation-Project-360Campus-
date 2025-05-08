from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
from main.models import *
from django.utils.crypto import get_random_string 
from django.utils import timezone
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

class MyClassTestCase(APITestCase):

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

        # Professor
        random_suffix = get_random_string(length=5)
        self.professor = Professor.objects.create(
            username=f'professor{random_suffix}',
            email=f'professor{random_suffix}@example.com',
            person_type='P',
            faculty=self.faculty,
            department='Engineering Department'
        )

        # Student
        random_suffix = get_random_string(length=5)
        self.student = Student.objects.create(
            username=f'student{random_suffix}',
            email=f'student{random_suffix}@example.com',
            person_type='S',
            faculty=self.faculty,
            department='Engineering Department'
        )

        # TA
        random_suffix = get_random_string(length=5)
        self.ta = TeachingAssistant.objects.create(
            username=f'ta{random_suffix}',
            email=f'ta{random_suffix}@example.com',
            person_type='T',
            department='Engineering Department'  # Use department instead of faculty
        )

        # Course
        self.course = Course.objects.create(
            title='Test Course',
            description='Test course description',
            college=self.college,
            level=1,
            semester_kind='F',
            prof=self.professor
        )

        # Semester
        self.semester = Semester.objects.create(
            kind='F',
            year=2025
        )

        # Classroom
        self.classroom = Classroom.objects.create(
            course=self.course,
            instructor=self.professor,
            semester=self.semester,
            rating=4.0
        )
        self.classroom.students.add(self.student)
        self.classroom.teaching_assistants.add(self.ta)

        # Token for professor
        token = Token.objects.create(user=self.professor)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        self.class_list_url = reverse('professor:class_list')
        self.class_detail_url = reverse('professor:class_detail', kwargs={'pk': self.course.pk})
        self.chatroom_url = reverse('professor:get_chatroom', kwargs={'pk': self.course.pk})
        self.participants_url = reverse('professor:get_participants', kwargs={'pk': self.course.pk})
        self.messages_url = reverse('professor:chat_messages', kwargs={'pk': self.course.pk})

    def tearDown(self):
        Material.objects.all().delete()
        Course.objects.all().delete()
        Professor.objects.all().delete()
        Student.objects.all().delete()
        TeachingAssistant.objects.all().delete()
        Classroom.objects.all().delete()
        Semester.objects.all().delete()
        get_user_model().objects.all().delete()
        Faculty.objects.all().delete()
        College.objects.all().delete()
        shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'Test Course'), ignore_errors=True)

    def test_class_list_success(self):
        response = self.client.get(self.class_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Course')
        self.assertEqual(response.data[0]['description'], 'Test course description')

    def test_class_list_unauthorized(self):
        self.client.credentials()
        response = self.client.get(self.class_list_url)
        self.assertEqual(response.status_code, 401)

    def test_class_detail_success(self):
        lecture_file = SimpleUploadedFile('lecture.pdf', b'Dummy lecture content', content_type='application/pdf')
        lab_file = SimpleUploadedFile('lab.pdf', b'Dummy lab content', content_type='application/pdf')
        self.client.post(
            reverse('professor:upload_material_by_type', kwargs={'pk': self.course.pk}),
            {
                'week_number': '1',
                'material_type': 'L',
                'file': lecture_file
            },
            format='multipart'
        )
        self.client.post(
            reverse('professor:upload_material_by_type', kwargs={'pk': self.course.pk}),
            {
                'week_number': '1',
                'material_type': 'l',
                'file': lab_file
            },
            format='multipart'
        )

        response = self.client.get(self.class_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('course', response.data)
        self.assertIn('materials_by_week', response.data)
        self.assertEqual(response.data['course']['title'], 'Test Course')
        self.assertEqual(len(response.data['materials_by_week']), 1)
        self.assertEqual(response.data['materials_by_week'][0]['week'], 1)
        self.assertEqual(len(response.data['materials_by_week'][0]['material_types']), 6)
        lecture_type = next(mt for mt in response.data['materials_by_week'][0]['material_types'] if mt['type'] == 'L')
        lab_type = next(mt for mt in response.data['materials_by_week'][0]['material_types'] if mt['type'] == 'l')
        self.assertTrue(lecture_type['has_materials'])
        self.assertTrue(lab_type['has_materials'])
        self.assertEqual(len(lecture_type['materials']), 1)
        self.assertEqual(len(lab_type['materials']), 1)
        self.assertEqual(lecture_type['materials'][0]['name'], 'lecture.pdf')
        self.assertEqual(lab_type['materials'][0]['name'], 'lab.pdf')

    def test_class_detail_no_materials(self):
        response = self.client.get(self.class_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('course', response.data)
        self.assertIn('materials_by_week', response.data)
        self.assertEqual(len(response.data['materials_by_week']), 0)

    def test_class_detail_unauthorized(self):
        self.client.credentials()
        response = self.client.get(self.class_detail_url)
        self.assertEqual(response.status_code, 401)

    def test_delete_material_success(self):
        lecture_file = SimpleUploadedFile('lecture.pdf', b'Dummy lecture content', content_type='application/pdf')
        self.client.post(
            reverse('professor:upload_material_by_type', kwargs={'pk': self.course.pk}),
            {
                'week_number': '1',
                'material_type': 'L',
                'file': lecture_file
            },
            format='multipart'
        )
        material = Material.objects.get(course=self.course, name='lecture.pdf')

        delete_url = reverse('professor:delete_material', kwargs={'pk': self.course.pk, 'material_id': material.id})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['detail'], 'Material deleted successfully.')
        self.assertFalse(Material.objects.filter(id=material.id).exists())

    def test_delete_material_unauthorized(self):
        lecture_file = SimpleUploadedFile('lecture.pdf', b'Dummy lecture content', content_type='application/pdf')
        self.client.post(
            reverse('professor:upload_material_by_type', kwargs={'pk': self.course.pk}),
            {
                'week_number': '1',
                'material_type': 'L',
                'file': lecture_file
            },
            format='multipart'
        )
        material = Material.objects.get(course=self.course, name='lecture.pdf')

        self.client.credentials()
        delete_url = reverse('professor:delete_material', kwargs={'pk': self.course.pk, 'material_id': material.id})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, 401)

    def test_upload_material_by_type_success(self):
        lecture_file = SimpleUploadedFile('lecture.pdf', b'Dummy lecture content', content_type='application/pdf')
        response = self.client.post(
            reverse('professor:upload_material_by_type', kwargs={'pk': self.course.pk}),
            {
                'week_number': '1',
                'material_type': 'L',
                'file': lecture_file
            },
            format='multipart'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['detail'], 'Material uploaded successfully.')
        material_exists = Material.objects.filter(
            course=self.course,
            name='lecture.pdf',
            week=1,
            material_type='L',
            created_by=self.professor
        ).exists()
        self.assertTrue(material_exists)

    def test_upload_material_by_type_missing_data(self):
        response = self.client.post(
            reverse('professor:upload_material_by_type', kwargs={'pk': self.course.pk}),
            {
                'week_number': '1',
                'material_type': 'L',
            },
            format='multipart'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Week number, material type, and file are required.')

    def test_upload_material_by_type_invalid_type(self):
        lecture_file = SimpleUploadedFile('lecture.pdf', b'Dummy lecture content', content_type='application/pdf')
        response = self.client.post(
            reverse('professor:upload_material_by_type', kwargs={'pk': self.course.pk}),
            {
                'week_number': '1',
                'material_type': 'X',
                'file': lecture_file
            },
            format='multipart'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Invalid material type.')

    def test_upload_material_by_type_unauthorized(self):
        lecture_file = SimpleUploadedFile('lecture.pdf', b'Dummy lecture content', content_type='application/pdf')
        self.client.credentials()
        response = self.client.post(
            reverse('professor:upload_material_by_type', kwargs={'pk': self.course.pk}),
            {
                'week_number': '1',
                'material_type': 'L',
                'file': lecture_file
            },
            format='multipart'
        )
        self.assertEqual(response.status_code, 401)

    # Chat Tests

    def test_get_chatroom_success(self):
        response = self.client.get(self.chatroom_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('chatroom_id', response.data)
        self.assertEqual(response.data['title'], 'Test Course Chatroom')
        self.assertEqual(response.data['course_id'], self.course.id)

    def test_get_chatroom_unauthorized(self):
        # Create a non-participant user
        random_suffix = get_random_string(length=5)
        non_participant = Professor.objects.create(
            username=f'nonparticipant{random_suffix}',
            email=f'nonparticipant{random_suffix}@example.com',
            person_type='P',
            faculty=self.faculty,
            department='Engineering Department'
        )
        token = Token.objects.create(user=non_participant)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        response = self.client.get(self.chatroom_url)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'You are not a participant in this course.')

    def test_get_participants_success(self):
        response = self.client.get(self.participants_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)  # Professor, TA, Student
        participants = sorted(response.data, key=lambda x: x['role'])
        self.assertEqual(participants[0]['role'], 'Professor')
        self.assertEqual(participants[0]['username'], self.professor.username)
        self.assertEqual(participants[1]['role'], 'Student')
        self.assertEqual(participants[1]['username'], self.student.username)
        self.assertEqual(participants[2]['role'], 'Teaching Assistant')
        self.assertEqual(participants[2]['username'], self.ta.username)

    def test_get_participants_unauthorized(self):
        random_suffix = get_random_string(length=5)
        non_participant = Professor.objects.create(
            username=f'nonparticipant{random_suffix}',
            email=f'nonparticipant{random_suffix}@example.com',
            person_type='P',
            faculty=self.faculty,
            department='Engineering Department'
        )
        token = Token.objects.create(user=non_participant)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        response = self.client.get(self.participants_url)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'You are not a participant in this course.')

    def test_get_messages_success(self):
        # Send a message first
        self.client.post(self.messages_url, {'content': 'Hello, class!'}, format='json')

        response = self.client.get(self.messages_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], 'Hello, class!')
        self.assertEqual(response.data[0]['sender']['username'], self.professor.username)
        self.assertEqual(response.data[0]['sender']['role'], 'P')

    def test_send_message_success(self):
        response = self.client.post(self.messages_url, {'content': 'Welcome to the course!'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['content'], 'Welcome to the course!')
        self.assertEqual(response.data['sender']['username'], self.professor.username)
        self.assertEqual(response.data['sender']['role'], 'P')

        # Verify the message exists in the database
        message_exists = Message.objects.filter(
            chatroom__course=self.course,
            sender=self.professor,
            content='Welcome to the course!'
        ).exists()
        self.assertTrue(message_exists)

    def test_send_message_missing_content(self):
        response = self.client.post(self.messages_url, {}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Message content is required.')

    def test_chat_messages_unauthorized(self):
        random_suffix = get_random_string(length=5)
        non_participant = Professor.objects.create(
            username=f'nonparticipant{random_suffix}',
            email=f'nonparticipant{random_suffix}@example.com',
            person_type='P',
            faculty=self.faculty,
            department='Engineering Department'
        )
        token = Token.objects.create(user=non_participant)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        # Test GET
        response = self.client.get(self.messages_url)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'You are not a participant in this course.')

        # Test POST
        response = self.client.post(self.messages_url, {'content': 'Unauthorized message'}, format='json')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'You are not a participant in this course.')

class EventTestCase(APITestCase):

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

        # Professor
        random_suffix = get_random_string(length=5)
        self.professor = Professor.objects.create(
            username=f'professor{random_suffix}',
            email=f'professor{random_suffix}@example.com',
            person_type='P',
            faculty=self.faculty,
            department='Engineering Department'
        )

        # Student
        random_suffix = get_random_string(length=5)
        self.student = Student.objects.create(
            username=f'student{random_suffix}',
            email=f'student{random_suffix}@example.com',
            person_type='S',
            faculty=self.faculty,
            department='Engineering Department'
        )

        # Event
        self.event = Event.objects.create(
            title='AI for Good Summit 2024',
            description='A summit on AI applications.',
            date=timezone.now() + timezone.timedelta(days=7)  # Future date
        )

        # Token for professor
        token = Token.objects.create(user=self.professor)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        self.events_url = reverse('professor:list_events')
        self.register_url = reverse('professor:event_register', kwargs={'pk': self.event.pk})

    def tearDown(self):
        Event.objects.all().delete()
        EventRegistration.objects.all().delete()
        Professor.objects.all().delete()
        Student.objects.all().delete()
        get_user_model().objects.all().delete()
        Faculty.objects.all().delete()
        College.objects.all().delete()

    def test_list_events_success(self):
        response = self.client.get(self.events_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'AI for Good Summit 2024')
        self.assertFalse(response.data[0]['is_registered'])  # Not registered yet

    def test_list_events_past_event(self):
        past_event = Event.objects.create(
            title='Past Event',
            description='An old event.',
            date=timezone.now() - timezone.timedelta(days=7)  # Past date
        )
        response = self.client.get(self.events_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Only future event should appear
        self.assertEqual(response.data[0]['title'], 'AI for Good Summit 2024')

    def test_event_register_success(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['detail'], 'Successfully registered for the event.')
        self.assertTrue(EventRegistration.objects.filter(person=self.professor, event=self.event).exists())

    def test_event_register_already_registered(self):
        EventRegistration.objects.create(person=self.professor, event=self.event)
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.data['detail'], 'Already registered for this event.')

    def test_event_register_past_date(self):
        past_event = Event.objects.create(
            title='Past Event',
            description='An old event.',
            date=timezone.now() - timezone.timedelta(days=7)
        )
        past_register_url = reverse('professor:event_register', kwargs={'pk': past_event.pk})
        response = self.client.post(past_register_url)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.data['detail'], 'Event date has passed.')

    def test_event_register_unauthorized(self):
        self.client.credentials()  # Remove authentication
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 401)
        
class GraduationProjectTestCase(APITestCase):

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

        # Professor
        random_suffix = get_random_string(length=5)
        self.professor = Professor.objects.create(
            username=f'professor{random_suffix}',
            email=f'professor{random_suffix}@example.com',
            person_type='P',
            faculty=self.faculty,
            department='Engineering Department'
        )

        # Token for professor
        token = Token.objects.create(user=self.professor)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        self.projects_url = reverse('professor:list_projects')
        self.add_project_url = reverse('professor:add_project')
        self.delete_project_url = lambda pk: reverse('professor:delete_project', kwargs={'pk': pk})

    def tearDown(self):
        GraduationProject.objects.all().delete()
        Professor.objects.all().delete()
        Faculty.objects.all().delete()
        College.objects.all().delete()
        get_user_model().objects.all().delete()

    def test_list_projects_empty(self):
        response = self.client.get(self.projects_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['empty'], True)
        self.assertEqual(len(response.data['projects']), 0)

    def test_list_projects_success(self):
        GraduationProject.objects.create(
            name='Campus-360',
            year=2025,
            faculty=self.faculty,
            description='Major: Computer Science with Artificial Intelligence',
            supervisor=self.professor,
            rate=3.75
        )
        response = self.client.get(self.projects_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['empty'], False)
        self.assertEqual(len(response.data['projects']), 1)
        self.assertEqual(response.data['projects'][0]['name'], 'Campus-360')
        self.assertEqual(response.data['projects'][0]['rate'], 3.75)

    def test_add_project_success(self):
        data = {
            'name': 'New Project',
            'year': 2025,
            'faculty': self.faculty.code,
            'description': 'A new graduation project',
            'rate': 3.90
        }
        response = self.client.post(self.add_project_url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['detail'], 'Project added successfully.')
        self.assertEqual(GraduationProject.objects.count(), 1)
        project = GraduationProject.objects.first()
        self.assertEqual(project.name, 'New Project')
        self.assertEqual(project.rate, 3.90)

    def test_add_project_missing_fields(self):
        data = {'name': 'Incomplete Project'}
        response = self.client.post(self.add_project_url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'All fields except rate are required.')

    def test_add_project_invalid_rate_range(self):
        data = {
            'name': 'Invalid Rate Project',
            'year': 2025,
            'faculty': self.faculty.code,
            'description': 'Invalid rate',
            'rate': 4.50
        }
        response = self.client.post(self.add_project_url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Rate must be between 0.00 and 4.00.')

    def test_add_project_negative_rate(self):
        data = {
            'name': 'Negative Rate Project',
            'year': 2025,
            'faculty': self.faculty.code,
            'description': 'Negative rate',
            'rate': -1.00
        }
        response = self.client.post(self.add_project_url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Rate must be between 0.00 and 4.00.')

    def test_add_project_success(self):
        data = {
            'name': 'New Project',
            'year': 2025,
            'faculty': self.faculty.code,
            'description': 'A new graduation project',
            'rate': 3.90
        }
        response = self.client.post(self.add_project_url, data, format='json')
        print("Response data:", response.data)  # Debug print
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['detail'], 'Project added successfully.')
        self.assertEqual(GraduationProject.objects.count(), 1)
        project = GraduationProject.objects.first()
        self.assertEqual(project.name, 'New Project')
        self.assertEqual(project.rate, 3.90)

    def test_delete_project_unauthorized(self):
        other_professor = Professor.objects.create(
            username='other_prof',
            email='other@example.com',
            person_type='P',
            faculty=self.faculty,
            department='Engineering Department'
        )
        project = GraduationProject.objects.create(
            name='Other Project',
            year=2025,
            faculty=self.faculty,
            description='Other project',
            supervisor=other_professor
        )
        response = self.client.delete(self.delete_project_url(project.id))
        self.assertEqual(response.status_code, 404)