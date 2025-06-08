import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_django.settings')
django.setup()
fake = Faker()

number = 20
from django.contrib.auth.models import User

# Liste d'utilisateurs à créer (username, password)
users = [
    ("hana", "password"),
    ("yaj", "password"),
    ("jeff", "password"),
]
user = [(fake.name(),'password') for _ in range(10)]

for username, password in user:
    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username=username, password=password)
        print(f"Utilisateur {username} créé.")
    else:
        print(f"Utilisateur {username} existe déjà.")
