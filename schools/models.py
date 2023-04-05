from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField()
    reservations = models.ManyToManyField(User, through='Reservation')

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    date = models.DateField()