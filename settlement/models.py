from django.db import models
from order.models import Order  # assuming settlements are tied to orders

class Settlement(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='settlement')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    settled_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')])

    def __str__(self):
        return f"Settlement for Order {self.order.id}"
