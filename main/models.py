# Create your models here.
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=30)
    price= models.IntegerField()
    category = models.CharField(max_length=100, blank=True)