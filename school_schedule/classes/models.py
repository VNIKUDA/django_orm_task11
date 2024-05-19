from django.db import models

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=3)
    year = models.IntegerField()

    def __str__(self):
        return self.name
