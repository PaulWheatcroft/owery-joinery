from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A user profile model for maintaining order history
    """
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_phone_number = models.CharField(
        max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username
