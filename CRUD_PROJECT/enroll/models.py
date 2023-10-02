from django.db import models


# Create your models here.
class User(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    Age = models.PositiveIntegerField()
    email = models.EmailField(max_length=70)
    pincode = models.IntegerField()
    Address = models.CharField(max_length=70)
    phone = models.PositiveIntegerField()
