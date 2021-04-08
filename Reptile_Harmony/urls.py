"""Reptile_Harmony URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
# our custom urls are pulls from apps
from home.views import home_view
# pulls our custom vars in settings
from django.conf import settings
from django.conf.urls.static import static

# then places in url patterns
urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
# the line above creates live urls for our images, and is not suggested for production use.