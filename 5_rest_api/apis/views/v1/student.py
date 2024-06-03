from rest_framework import viewsets,filters,generics
from apis.models import Student
from apis.serializers import StudentSerializer,StudentDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name','surname','gender','school','classroom']
    search_fields = ['name','surname','gender','school','classroom']

class StudentDetailView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer