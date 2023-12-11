from django.db import models
from django.utils.timezone import now

statuses = (
    ('Pending', 'Pending'),
    ('Failed', 'Failed'),
    ('Success', 'Success')
)

class Payment(models.Model):
    Amount = models.IntegerField()
    Date = models.DateTimeField(default=now)
    Status = models.CharField(choices=statuses, max_length=100)
