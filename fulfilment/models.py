from django.db import models
from customer.models import Customer
from courier.models import Courier
from delivery.models import Delivery


class Fulfilment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    fulfilled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"{self.customer} - {self.status}"
