from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hello.models import LogMessage
from hello.models import Tweet, Comment, Like


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
        fields= ['content', 'image']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = [] 