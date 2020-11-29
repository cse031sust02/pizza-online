from authentication.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ManagerRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
