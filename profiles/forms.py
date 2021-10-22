from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    """
    Extends the sign-up form to include first and last names
    """
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    mobile_number = forms.CharField(max_length=12, label='Phone Number', required=None)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.mobile_number = self.cleaned_data['mobile_number']
        user.save()
        return user
