from django.db import models
from django.utils.timezone import now

statuses = (
    ('Pending', 'Pending'),
    ('Cancelled', 'Cancelled'),
    ('Done', 'Done')
)

class Reservation(models.Model):
    Client = models.ForeignKey('Clients.Client', models.CASCADE)
    Reserved_On = models.DateTimeField(default=now)
    Date_of_Reservation = models.DateTimeField()
    Number_of_People = models.IntegerField()
    Deposit_Paid = models.ForeignKey('Payments.Payment', models.CASCADE)
    Status = models.CharField(choices=statuses, max_length=100)