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
