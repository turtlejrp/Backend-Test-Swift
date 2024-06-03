from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.v1.school import SchoolViewSet,ClassroomViewSet,SchoolDetailView,ClassroomDetailView
from .views.v1.teacher import TeacherViewSet,TeacherDetailView
from .views.v1.student import StudentViewSet,StudentDetailView

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'classrooms', ClassroomViewSet, basename='classroom')
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'students', StudentViewSet, basename='student')

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls)),
    path('v1/schools/detail/<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    path('v1/classroom/detail/<int:pk>/', ClassroomDetailView.as_view(), name='classroom-detail'),
    path('v1/teacher/detail/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('v1/student/detail/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]
