import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView
from .models import Tweet, Like, Follow
from hello.forms import SignUpForm, TweetForm, CommentForm, LikeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
    form = TweetForm(request.POST, request.FILES)
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "hello/home.html", {"tweets":tweets})

@login_required
def profile(request):
    user_tweets = Tweet.objects.filter(user= request.user).order_by("-created_at")
    return render(request, "hello/profile.html", {"user": request.user, "tweets":user_tweets})


def profile_detail(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    user_tweets = Tweet.objects.filter(user=profile_user).order_by('-created_at')
    is_following = False
    if request.user.is_authenticated and request.user != profile_user:
        is_following = Follow.objects.filter(follower=request.user, following=profile_user).exists()
    return render(request, "hello/profile_detail.html", {
        "profile_user": profile_user,
        "tweets": user_tweets,
        "is_following": is_following,
    })
    
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
    
@login_required
def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    comments = tweet.comments.all().order_by("-created_at")
    has_liked = tweet.likes.filter(user=request.user).exists()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment.form.save(commit=False)
            comment.tweet = tweet
            comment.user = request.user
            comment.save()
            return redirect('tweet_detail', tweet_id=tweet.id)
    else:
        comment_form = CommentForm()
    return render(request, "hello/tweet_detail.html", {
        "tweet": tweet,
        "comments": comments,
        "comment_form": comment_form,
        "has_liked": has_liked,
    })

@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    like, created = Like.objects.get_or_create(tweet=tweet, user=request.user)
    if not created:
        like.delete()
    else:  
        like.save()
    return redirect('tweet_detail', tweet_id=tweet.id)

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user != user_to_follow:
        follow, created = Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
        if not created:
            follow.delete()
    return redirect('profile_detail', user_id=user_to_follow.id)

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    if request.user != user_to_unfollow:
        follow = Follow.objects.filter(follower= request.user, following = user_to_unfollow).first()
        if follow:
            follow.delete()
    return redirect('profile_detail', user_id=user_to_unfollow.id)
@login_required
def following_list(request):
    following = Follow.objects.filter(follower=request.user)
    following_users = [follow.following for follow in following]
    tweets = Tweet.objects.filter(user__in=following_users).order_by("-created_at")
    return render(request, "hello/following_list.html", {"tweets": tweets})