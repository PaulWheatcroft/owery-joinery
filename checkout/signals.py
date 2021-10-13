from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItems


@receiver(post_save, sender=OrderLineItems)
def update_on_save(sender, instance, created, **kwargs):
    """
    sender = OrderLineItem
    instance = model that sent the signal
    created = boolean as to whether this is new or be updated
    and any key work args
    Update order total when line items are created or updated
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItems)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total when line items are deleted
    """
    instance.order.update_total()
