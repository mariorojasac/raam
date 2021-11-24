from django.db import models

# Create your models here.

class Pantry(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.TextField(max_length=250)