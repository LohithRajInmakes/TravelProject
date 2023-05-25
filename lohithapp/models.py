from django.db import models

# Create your models here.
class Place(models.Model):
    title=models.CharField(max_length=500)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()

    def __str__(self):
        return self.title

class Person(models.Model):
    name=models.CharField(max_length=500)
    photo=models.ImageField(upload_to='pics')
    detail=models.TextField()

    def __str__(self):
        return self.name

