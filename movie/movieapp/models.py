from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=300)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='moviegallery')

def __str__(self):
    return self.name
