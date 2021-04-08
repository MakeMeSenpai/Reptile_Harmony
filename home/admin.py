from django.contrib import admin
# pulls from your models
# note that because it's in the same file we can use .module However we could also use home.module
from .models import Home

# Model Admin represents the models presence in the admin page. This is not needed if there is
# no customizations
# class HomeAdmin(admin.ModelAdmin):
#     pass

'''to see your database in shell use $python3 manage.py shell then 
>> from home.models import Home
>> Home.objects.all()
You can then create more objects using create, and passing all required inputs as seen below
>> Home.objects.create(summary="My new object", img="image/link", imga="image/link", imgb="image/link", imgc="image/link", info="My new object")'''
admin.site.register(Home)  # HomeAdmin) # Needed when there is customizations