from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    User profile contains default user details to
    associate with order information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)  

    def __str__(self):
        return self.user.username
