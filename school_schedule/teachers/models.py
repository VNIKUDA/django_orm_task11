from django.db import models
import sys
sys.path.append("..")
from subjects.models import Subject

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, related_name="teachers", on_delete=models.CASCADE)
