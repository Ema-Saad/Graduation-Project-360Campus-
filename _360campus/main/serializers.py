from rest_framework.serializers import ModelSerializer
from .models import *

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class GraduationProjectSerializer(ModelSerializer):
    class Meta:
        model = GraduationProject
        fields = '__all__'  # Includes all fields from the model

class CourseViewSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ['admin', 'created_at', 'updated_at']
        depth = 1

class ClassroomViewSerializer(ModelSerializer):
    class Meta:
        model = Classroom
        exclude = ['students', 'id']
        depth = 1

class TaskViewSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ['classroom']

class AssignmentSerializer(ModelSerializer):
    task = TaskViewSerializer(read_only=True)

    class Meta:
        model = Assignment
        exclude = ['submissions']

class AssignmentSubmissionViewSerializer(ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['submitted_file', 'grade']


class CollegeSerializer(ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'
        depth = 1
