from django.contrib import admin
# pull from your models
from website.models import Home

# Model Admin represents the models presence in the admin page. This is not needed if there is
# no customizations
# class HomeAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Home)  # HomeAdmin) #Needed when there is customizations