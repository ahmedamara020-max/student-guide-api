from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DepartmentViewSet, StudentViewSet, SubjectViewSet, 
    ScheduleViewSet, ExamViewSet, TodoViewSet,
    RegisterView, LoginWithCookieView, LogoutView,
)


router = DefaultRouter()

router.register(r'departments', DepartmentViewSet)
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'todos', TodoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginWithCookieView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]

