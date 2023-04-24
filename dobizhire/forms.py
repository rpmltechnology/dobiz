from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from dobizhire.models import *
from django import forms

class JobApplication(forms.ModelForm):
    class Meta:
        model =AppliedForJobs
        fields = ('jobrole','fname','lname','email','phone','address','city','msg','files')
