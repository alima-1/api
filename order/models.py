from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.order_number
