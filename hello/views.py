import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView
from .models import Tweet
from hello.forms import SignUpForm, TweetForm
from django.contrib.auth.decorators import login_required

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "hello/about.html")


# Add this code elsewhere in the file:
def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})

@login_required
def home(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "hello/home.html", {"tweets":tweets})

@login_required
def profile(request):
    user_tweets = Tweet.objects.filter(user= request.user).order_by("-created_at")
    return render(request, "hello/profile.html", {"user": request.user, "tweets":user_tweets})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUpForm()
        return render(request, "registration/signup.html", {"form": form})
    
@login_required
def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit= False)
            tweet.user = request.user
            tweet.save()
            return redirect('home')
    else:
        form = TweetForm()
        return render(request, "hello/create_tweet.html", {"form": form})