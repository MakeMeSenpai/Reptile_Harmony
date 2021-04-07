import datetime
from django.db import models
from django.utils import timezone

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
    img = models.ImageField(name="cone")
    imga = models.ImageField(name="ctwo")
    imgb = models.ImageField(name="cthree")
    imgc = models.ImageField(name="cfour")
    info = models.CharField(max_length=650)

    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.summary
    def __cone__(self):
        return self.img
    def __ctwo__(self):
        return self.imga
    def __cthree__(self):
        return self.imgb
    def __cfour__(self):
        return self.imgc
    def __info__(self):
        return self.info
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'