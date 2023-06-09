from rest_framework.serializers import ModelSerializer
from .models import *


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'


class NewSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class GallarySerializer(ModelSerializer):
    class Meta:
        model = Gallary
        fields = '__all__'