from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hello.models import LogMessage


class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")