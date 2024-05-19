from django.db import models
import sys
sys.path.append("..")
from teachers.models import Teacher
from subjects.models import Subject
from classes.models import Class

# Create your models here.
class Schedule(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    week_day = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    current_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day_of_week} - {self.start_time} - {self.subject}"
