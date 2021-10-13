from django.contrib import admin
from .models import Order, OrderLineItems

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderLineItems)
