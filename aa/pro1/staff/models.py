
from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)

