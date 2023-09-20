from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfiles

class LoginForm(forms.ModelForm):
    email = forms.CharField(max_length=254,  error_messages={'required': 'email is required'})
    password = forms.CharField(  widget=forms.PasswordInput(), error_messages={'required': 'Password is required'})

    class Meta:
        model = User
        fields = ("email", "password")


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30,  error_messages={'required': 'Username is required'})
    first_name = forms.CharField(max_length=30,  error_messages={'required': 'First name is required'})
    last_name = forms.CharField(max_length=30,  error_messages={'required': 'Last name is required'})
    email = forms.EmailField(max_length=254,  error_messages={'required': 'Email is required'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
        
        class Meta:
            model = UserProfiles
            fields = ("image",)

