from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import *
from django import forms

import re

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('fname','lname','email','phone',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("User with this email already exists")
        except User.DoesNotExist:
            return email

class ContactUser(forms.ModelForm):
    class Meta:
        model =Contact
        fields = ('name','email','phone','state','comment')

class ProfileUser(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('fname','lname','dob','email','mobile','Services', 'Business', 'Think_to_start_business','address','area','city','country','pin','state')
    
    def __init__(self, *args, **kwargs):
        super(ProfileUser, self).__init__(*args, **kwargs)
        if 'initial' in kwargs:
            initial = kwargs['initial']
            self.fields['fname'].initial = initial['fname']
            self.fields['lname'].initial = initial['lname']
            self.fields['email'].initial = initial['email']
            self.fields['mobile'].initial = initial['mobile']

class PasswordResetForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")