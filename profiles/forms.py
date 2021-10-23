from django import forms


class ProfileDetails(forms.ModelForm):
    """
    Extends the sign-up form to include first and last names
    """
    profile_mobile_number = forms.CharField(max_length=12, label='Phone Number', required=None)
