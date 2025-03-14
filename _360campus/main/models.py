from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class Person(AbstractUser):
    PERSON_TYPE_CHOICES = [
        ('S', 'Student'),
        ('P', 'Professor'),
        ('T', 'Teaching Assistant'),
        ('A', 'Admin'),
    ]

    department = models.CharField(max_length=50, null=True, blank=True)
    person_type = models.CharField(max_length=1, choices=PERSON_TYPE_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['person_type', 'department']

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"

class Professor(Person):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Professor"

class GraduationProject(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    description = models.TextField()
    supervisor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True, related_name="supervised_projects" )
    rate = models.DecimalField(max_digits=3, decimal_places= 2 , default= 0.00)
    
    class Meta:
        verbose_name = "Graduation Project"
        ordering = ["-rate"]
        
        
class Student(Person):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    graduation_project = models.ForeignKey(GraduationProject, on_delete=models.SET_NULL, null=True, blank=True, related_name="students")
    class Meta:
        verbose_name = "Student"


class TeachingAssistant(Person):
    class Meta:
        verbose_name = "Teaching Assistant"


class Admin(Person):
    class Meta:
        verbose_name = "Admin"


class College(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    chairman = models.ForeignKey(Professor, on_delete=models.SET_NULL, related_name="dean_of_college", null=True, blank=True)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    description = models.TextField()
    head = models.ForeignKey(Professor, on_delete=models.SET_NULL, related_name="head_of_faculty", null=True, blank=True)

    def __str__(self):
        return self.name

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


class Semester(models.Model):
    SEMESTER_TYPE = [
        ('F', 'Fall'),
        ('S', 'Spring'),
        ('s', 'Summer'),
    ]

    kind = models.CharField(max_length=1, choices=SEMESTER_TYPE)
    year = models.IntegerField()

# Course Model
class Course(models.Model):

    LEVELS = [(i, f'{i}') for i in range(1, 5)]
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, blank=True, related_name="courses")
    prerequisites = models.ManyToManyField('self', symmetrical=False, related_name="required_for", blank=True)
    # I added New fields to filter matrials
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    level = models.IntegerField(choices=LEVELS)
    semester_kind = models.CharField(max_length=1, choices=Semester.SEMESTER_TYPE)

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
    students = models.ManyToManyField(Student)

    class Meta:
        verbose_name = 'Classroom'



class Material(models.Model):
    # I added this function to avoid the SuspiciousFileOperation error
    def get_materials_file_location(inst, filename):
    # Include the filename in the path so that the full path is valid
        return f'{inst.classroom.title}/{filename}'
    course =models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    file = models.FileField(upload_to=get_materials_file_location)
    week = models.IntegerField(null=True, blank=True)  
    material_type = models.CharField(max_length=50, null=True, blank=True)#"Lecture", "Tutorial", "Lab", "assignment".


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
        



class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    max_grade = models.IntegerField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    submissions = models.ManyToManyField(Student, through='AssignmentSubmission', related_name='submissions')
    comments = models.ManyToManyField(Student, through='AssignmentComment', related_name='comments')

class AssignmentSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submitted_file = models.FileField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)


class AssignmentComment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    comment = models.TextField()
    is_private = models.BooleanField(null=True)
