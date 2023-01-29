from django.db import models

class User(models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    email=models.CharField(max_length=100,default="")
    payment_id=models.CharField(max_length=100)
# Create your models here.
