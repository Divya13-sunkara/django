from django.db import models

class Fee(models.Model):
    student_name = models.CharField(max_length=100)
    amount = models.IntegerField()

