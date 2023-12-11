from django.db import models

class Drink(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()