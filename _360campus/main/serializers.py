from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'first_name',
            'last_name',
            'department',
            'person_type',
            'email',
        ]

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class MaterialSerializer(ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Material
        fields = '__all__'

class GraduationProjectSerializer(ModelSerializer):
    class Meta:
        model = GraduationProject
        fields = '__all__'  # Includes all fields from the model

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ['admin']
        depth = 1

class CourseEditSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'description']

class ClassroomViewSerializer(ModelSerializer):
    instructor = PersonSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Classroom
        exclude = ['students']
        depth = 1

class TaskViewSerializer(ModelSerializer):
    classroom = ClassroomViewSerializer()

    class Meta:
        model = Task
        fields = '__all__'

class TaskModifySerializer(ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.filter(semester=Semester.objects.last())
    )

    class Meta:
        model = Task
        fields = '__all__'


class AssignmentSerializer(ModelSerializer):
    classroom = ClassroomViewSerializer()

    class Meta:
        model = Assignment
        exclude = ['submissions']

class AssignmentCreateSerializer(ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.filter(semester=Semester.objects.last())
    )

    class Meta:
        model = Assignment
        exclude = ['submissions']

class AssignmentModifySerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'max_grade', 'time']

class AssignmentSubmissionViewSerializer(ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['submitted_file', 'grade']

class CollegeSerializer(ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'
        depth = 1

class SchedulePreferenceSerializer(ModelSerializer):
    class Meta:
        model = SchedulePreference
        fields = '__all__'

class SchedulePreferenceViewSerializer(ModelSerializer):
    class Meta:
        model = SchedulePreference
        fields = ['slot', 'day']
