from django.db import models
from courses.models import Course
from django.core.validators import RegexValidator

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator(regex=r'^[A-Za-z\s]+$', message='Name must contain only letters and spaces.')]
    )
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to='students/', blank=True, null=True)
    date_of_birth = models.DateField()

   
    courses = models.ManyToManyField(
        Course,
        through='StudentCourse',
        related_name='students'
    )

    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course  = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} ↔ {self.course}"
