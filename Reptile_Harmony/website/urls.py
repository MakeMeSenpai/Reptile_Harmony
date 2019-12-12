from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('shop/', views.shop, name="shop"),
    path('cart/', views.cart, name="cart"),
    # path('info/', views.index, name="info"), #edit to go to #info
    # path('about/', views.other, name="about"), #edit to go to about
    path('other/', views.other, name="other"),
]
