from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DepartmentViewSet, StudentViewSet, SubjectViewSet, 
    ScheduleViewSet, ExamViewSet, TodoViewSet
)

# 1. بنعمل نسخة من الـ Router
router = DefaultRouter()

router.register(r'departments', DepartmentViewSet)
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'todos', TodoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

