from django.db import models
import sys
sys.path.append("..")
from classes.models import Class
# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, related_name="students", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.first_name