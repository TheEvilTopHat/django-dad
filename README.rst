==========
Django Dad
==========

Django Dad is a simple Django app to add a dad joke to the admin home page.
It uses https://icanhazdadjoke.com/ to get the jokes.

Quick start
-----------

1. Add "django-dad" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django-dad',
    ]

2. Now go to your admin page and login, you should now see a new dad joke in the title area.