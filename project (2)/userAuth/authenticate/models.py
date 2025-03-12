from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fooddb123(models.Model):
    food_typeq=[('veg','VEG'),('non-veg','NON-VEG'),('both','BOTH')]
    user = models.ForeignKey(to=User,on_delete=models.CASCADE, related_name="form", blank=True, null=True)
    name=models.CharField(max_length=20)
    mobile= models.IntegerField()
    quantity=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=40)
    food_type=models.CharField(max_length=10,choices=food_typeq,null=True)
