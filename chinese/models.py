from django.db import models

# Create your models here.

class Category(models.Model):
    name = models. CharField(max_length=20)

    def __str__(self):
        return self.name

class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,unique=True)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    


    