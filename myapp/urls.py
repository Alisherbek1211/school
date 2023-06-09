from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register('about',AboutViewSet)
router.register('teacher',TeacherViewSet)
router.register('news',NewViewSet)
router.register('gallary',GallaryViewSet)

urlpatterns = [
    path('',include(router.urls))
]