from django import forms
from checkout.models import OrderStatus, Order


class OrderStatusForm(forms.ModelForm):
    """
    Allow a staff member to change the satus of an order
    """
    class Meta:
        model = Order
        fields = ('status',)
