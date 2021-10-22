from django.contrib import admin
from .models import AdditionalUserDetails


class UserAdmin(admin.ModelAdmin):
    fields = (
        'user', 'phone_number', 'random_field',)

    list_display = (
        'user', 'phone_number', 'random_field',)


admin.site.register(AdditionalUserDetails, UserAdmin)
