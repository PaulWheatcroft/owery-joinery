from django import forms


class ProfileDetails(forms.ModelForm):
    """
    Extends the sign-up form to include first and last names
    """
    profile_first_name = forms.CharField(max_length=30, label='First Name')
    profile_last_name = forms.CharField(max_length=30, label='Last Name')
    profile_mobile_number = forms.CharField(max_length=12, label='Phone Number', required=None)
