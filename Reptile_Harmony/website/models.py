from django.db import models

# For future refference when using django:
# Create your models in app/models.py
# ensure that your app is in project/settings.py installed list.
# $python3 manage.py check
# $python3 manage.py makemigrations
# $python3 manage.py migrate
# Register your models in app/admin.py
# request your [models || database] at desired html view, in app/views.py

class Home(models.Model):
    summary = models.CharField(max_length=650)