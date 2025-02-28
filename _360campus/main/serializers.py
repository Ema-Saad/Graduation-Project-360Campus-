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