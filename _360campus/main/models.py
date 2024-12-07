from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


# Person model with Single Table Inheritance
class Person(AbstractBaseUser):
    PERSON_TYPE_CHOICES = [
        ('S', 'Student'),
        ('P', 'Professor'),
        ('T', 'Teaching Assistant'),
        ('A', 'Admin'),
    ]

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['person_type', 'department']

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    person_type = models.CharField(max_length=1, choices=PERSON_TYPE_CHOICES)

    objects = UserManager()

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"


class Student(Person):
    class Meta:
        verbose_name = "Student"


class Professor(Person):
    class Meta:
        verbose_name = "Professor"


class TeachingAssistant(Person):
    class Meta:
        verbose_name = "Teaching Assistant"


class Admin(Person):
    class Meta:
        verbose_name = "Admin"


# Report Model
class Report(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    data = models.JSONField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="reports")

    class Meta:
        verbose_name = "Report"


# Event Model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()

    class Meta:
        verbose_name = "Event"


# EventRegistration Model
class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="event_registrations")
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Event Registration"
        unique_together = ('event', 'student')


# Course Model
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, related_name="courses")
    prerequisites = models.ManyToManyField('self', symmetrical=False, related_name="required_for", blank=True)

    class Meta:
        verbose_name = "Course"


# Enrollment Model
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Enrollment"
        unique_together = ('student', 'course')


class Classroom(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Classroom'

def get_materials_file_location(inst, filename):
    return f'{inst.classroom.title}/'

class Material(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    file = models.FileField(upload_to=get_materials_file_location)


# Lecture Model
class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lectures")
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    duration = models.IntegerField()  # Duration in minutes

    class Meta:
        verbose_name = "Lecture"


# StaffPerformance Model
class StaffPerformance(models.Model):
    staff = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="performance_reviews")
    evaluation_score = models.FloatField()
    feedback = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Staff Performance"


# Chatroom Model
class Chatroom(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="chatrooms", null=True)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Chatroom"


# Message Model
class Message(models.Model):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Message"

