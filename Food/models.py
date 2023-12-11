from django.db import models

class Food(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='Food/Images')
