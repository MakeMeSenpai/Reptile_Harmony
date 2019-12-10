from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('shop/', views.shop),
    path('cart/', views.cart),
    path('other/', views.other),
]
