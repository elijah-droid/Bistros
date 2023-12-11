from django.db import models

class Dish(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='Images/Dishes')
    Price = models.IntegerField(null=True, blank=True)
    Foods = models.ManyToManyField('Food.Food')
    Description = models.TextField(max_length=10000)