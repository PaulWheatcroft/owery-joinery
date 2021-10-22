from django.contrib import admin
from django.contrib.auth.models import User
from .models import Order, OrderLineItems


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItems
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('user', 'order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart', 'stripe_pid')

    fields = ('user', 'order_number', 'date', 'first_name', 'last_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart', 'stripe_pid')

    list_display = ('user', 'order_number', 'date', 'first_name', 'last_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
