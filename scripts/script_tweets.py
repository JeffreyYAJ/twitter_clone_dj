import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_django.settings')
django.setup()

from django.contrib.auth.models import User
from hello.models import Tweet

users = list(User.objects.all())
messages = [
    "Hello Twitter !",
    "Ceci est un tweet automatique.",
    "Django c'est génial !",
    "Un autre tweet pour tester.",
    "Encore un tweet, parce que pourquoi pas ?",
    "Je découvre ce clone de Twitter.",
    "Automatisation des tests avec des tweets.",
    "Tweet tweet tweet !",
    "Python et Django, la combinaison parfaite.",
    "Dernier tweet de la série."
]

for i in range(50):  # Crée 50 tweets
    user = random.choice(users)
    content = random.choice(messages) + f" #{i+1}"
    Tweet.objects.create(user=user, content=content)
    print(f"Tweet créé pour {user.username}: {content}")
