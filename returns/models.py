from django.db import models
from order.models import OrderItem


class Return(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    reason = models.TextField()
    returned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Return for OrderItem ID: {self.order_item.id}"
