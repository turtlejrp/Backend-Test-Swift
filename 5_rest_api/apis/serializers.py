from rest_framework import serializers
from .models import School,Classroom,Teacher,Student

# code here

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
    

class SchoolDetailSerializer(serializers.ModelSerializer):
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['name', 'abbreviation_name', 'address', 'classroom_count','teacher_count','student_count']

    def get_classroom_count(self, obj):
        return Classroom.objects.filter(school=obj).count()
    
    def get_teacher_count(self, obj):
        return Teacher.objects.filter(school=obj).count()
    
    def get_student_count(self, obj):
        return Student.objects.filter(school=obj).count()

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ClassroomDetailSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True, source='student_set')
    teachers = TeacherSerializer(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = ['classroom_year', 'classroom_room', 'school', 'students', 'teachers']

class TeacherDetailSerializer(serializers.ModelSerializer):
    classrooms = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='classroom_room'
    )

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'surname', 'gender', 'school', 'classrooms']


class StudentDetailSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'gender', 'school', 'classroom']
