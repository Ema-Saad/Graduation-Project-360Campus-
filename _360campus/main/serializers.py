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

class ClassroomSerializer(ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'
        depth = 1

class AssignmentSerializer(ModelSerializer):
    classroom = ClassroomSerializer(read_only=True)

    class Meta:
        model = Assignment
        exclude = ['submissions', 'comments']

class AssignmentSubmissionViewSerializer(ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['submitted_file', 'grade']

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ['admin']
        depth = 1


class CollegeSerializer(ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'
        depth = 1
