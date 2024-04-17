from django.db import models
from chinese.models import Food

# Create your models here.
class Cart(models.Model):
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()