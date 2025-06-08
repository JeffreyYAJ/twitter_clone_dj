from django.urls import path
from hello import views
from hello.models import LogMessage
from django.contrib.auth.decorators import login_required

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path('', views.home, name = "home"),
    path("about/", views.about, name="about"),
    path("log/", views.log_message, name="log"),
    path("signup/", views.signup, name= "signup"),
    path("profile", login_required(views.profile), name = "profile"),
    path("tweet/new/", views.create_tweet, name = "create_tweet")
    

]

