from django.contrib import admin
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):

    readonly_fields = ('user_profile',)

    fields = ('user_profile', 'profile_phone_number')

    list_display = ('user_profile', 'profile_phone_number')


admin.site.register(UserProfile, ProfileAdmin)
