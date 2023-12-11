from django.db import models

types = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
)

class Meal(models.Model):
    Type = models.CharField(choices=types, max_length=100)
    Dishes = models.ManyToManyField('Dishes.Dish')
