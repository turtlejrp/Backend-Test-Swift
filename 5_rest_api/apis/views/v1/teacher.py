from rest_framework import viewsets,filters,generics
from apis.models import Teacher
from apis.serializers import TeacherSerializer,TeacherDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name','surname','gender','school','classrooms']
    search_fields = ['name','surname','gender','school','classrooms']

class TeacherDetailView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer
