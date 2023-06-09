from django.shortcuts import render
from rest_framework.viewsets import  ModelViewSet
from .serializers import *
from .models import *


class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer


class NewViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewSerializer


class GallaryViewSet(ModelViewSet):
    queryset = Gallary.objects.all()
    serializer_class = GallarySerializer