from django import forms
from .models import CustomUser

# forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'profile_picture', 'birth_date']


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role', 'birth_date', 'profile_picture']

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'birth_date', 'profile_picture']
