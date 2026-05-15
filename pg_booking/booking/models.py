from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from pgapp.models import PG

class BOOKING(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    pg = models.ForeignKey(PG, on_delete=models.CASCADE)

    booking_date = models.DateField(auto_now_add=True)

    status=models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.user.username