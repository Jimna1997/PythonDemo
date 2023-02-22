from django.db import models
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=250,unique=True)
    overview = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)

class Student(models.Model):
    name = models.CharField(max_length=300)
    # dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=300)
    phn_no = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=300)
    dept = models.CharField(max_length=300)
    course = models.CharField(max_length=300)
    purpose = models.CharField(max_length=300)
    materials = models.CharField(max_length=300)

def __str__(self):
    return self.name
