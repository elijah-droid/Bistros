from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    User = models.OneToOneField(User, models.CASCADE)
    reservations = models.ManyToManyField('Reservations.Reservation')
