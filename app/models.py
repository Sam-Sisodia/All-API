from unicodedata import category
from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    price =models.IntegerField()


    def __str__(self):
        return self.name
    
    
