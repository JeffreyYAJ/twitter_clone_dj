from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hello.models import LogMessage
from hello.models import Tweet, Comment, Like
from .models import Message


class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': "Quoi de neuf ?",
                'class': 'tweet-input',
                'rows': 3,
            }),
        }
        labels = {
            'content': '',
        }       
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = [] 
        

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Votre message...'}),
        }