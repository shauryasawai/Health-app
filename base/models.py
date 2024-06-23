from django.db import models

# Create your models here.

class CallBooking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.date}"