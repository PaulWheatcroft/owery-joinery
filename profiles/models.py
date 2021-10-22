from django.db import models
from django.contrib.auth.models import User


class AdditionalUserDetails(models.Model):
    """
    User profile contains default user details to
    associate with order information
    """
    class Meta:
        """
        Fix django default addition of 's' for plural
        """
        verbose_name_plural = 'Additional user details'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    random_field = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username
