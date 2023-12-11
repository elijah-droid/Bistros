from django.db import models

class EmailVerification(models.Model):
    email = models.EmailField(max_length=100)
    code = models.IntegerField()