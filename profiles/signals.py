from django.dispatch import receiver
from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def create_user_profile():
    """
    sender = OrderLineItem
    instance = model that sent the signal
    created = boolean as to whether this is new or be updated
    and any key work args
    Creat a user profile when the Allauth signal is received
    """
    print('Hello Allauth Signal!')
