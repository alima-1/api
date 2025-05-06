from django.db import models

class Delivery(models.Model):
    delivery_date = models.DateTimeField()
    address = models.TextField()
    status = models.CharField(max_length=100, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('delivered', 'Delivered'),
    ])
    courier = models.ForeignKey('courier.Courier', on_delete=models.CASCADE)  # Link to Courier model
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)  # Link to Customer model

    def __str__(self):
        return f"Delivery to {self.customer} on {self.delivery_date}"
