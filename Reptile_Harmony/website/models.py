from django.db import models

# Create your models here.

class Home(models.Model):
    summary = models.CharField(max_length=650)