from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=200)
    