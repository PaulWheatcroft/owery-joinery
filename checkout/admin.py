from django.contrib import admin
from .models import Order, OrderLineItems, OrderStatus


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItems
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart', 'stripe_pid')

    fields = ('order_number', 'status', 'user_profile', 'date', 'first_name',
              'last_name', 'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart', 'stripe_pid')

    list_display = ('order_number', 'status', 'user_profile', 'date',
                    'first_name', 'last_name', 'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


class OrderStatusAdmin(admin.ModelAdmin):
    fields = ('status_id', 'status_name', 'status_description')

    list_display = ('status_id', 'status_name', 'status_description')

    ordering = ('status_id',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
