from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
# admin.site.register(Order)
admin.site.register(OrderItem)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ("order_number",)
