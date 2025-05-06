from django.db import models

class Courier(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
