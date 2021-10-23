from django.contrib import admin
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):

    fields = ('user', 'profile_phone_number')

    list_display = ('user', 'profile_phone_number')


admin.site.register(UserProfile, ProfileAdmin)
