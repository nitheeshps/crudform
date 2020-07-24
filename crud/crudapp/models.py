from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=25)
    Age = models.IntegerField()
    Dep = models.CharField(max_length=30)
    cgpa = models.IntegerField()
    project = models.CharField(max_length=25)
    clubs = models.CharField(max_length=25)
