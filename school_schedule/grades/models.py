from django.db import models
import sys
sys.path.append("..")
from subjects.models import Subject
from student.models import Student

# Create your models here.
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    grade = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student}, {self.subject}, {self.grade}"