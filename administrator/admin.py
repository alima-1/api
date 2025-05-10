from django.contrib import admin
from .models import Administrator

admin.site.register(Administrator)

# customize how the model appears and works in the admin (like adding filters, search, etc.).
# @admin.register(Administrator)
# class AdministratorAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'role', 'date_joined')
#     search_fields = ('first_name', 'last_name', 'email')
#     list_filter = ('is_active', 'role')
