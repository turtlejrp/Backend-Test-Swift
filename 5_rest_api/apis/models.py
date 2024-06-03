from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    abbreviation_name= models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name
    

class Classroom(models.Model):
    classroom_year = models.IntegerField()
    classroom_room= models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"Classroom {self.classroom_room} of {self.school.name}"
    

class Teacher(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ) 

    name = models.CharField(max_length=100)
    surname= models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Student(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ) 

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"