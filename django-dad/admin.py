from django.contrib import admin
from django.contrib.auth.signals import user_logged_in
import requests

def joke_machine(sender, user, request, **kwargs):
    #dad joke
    if user.is_superuser:
        r = requests.get('https://icanhazdadjoke.com/',headers={'Accept': 'text/plain'})
        r.encoding = 'utf-8'
        admin.site.index_title = r.text
user_logged_in.connect(joke_machine)

# Register your models here.
