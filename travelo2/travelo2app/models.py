from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()

class Team(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics1')
    inf=models.TextField()
