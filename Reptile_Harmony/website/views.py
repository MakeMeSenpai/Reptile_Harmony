from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
class IndexView(generic.DetailView):
    template_name = 'website/index'

class ShopView(generic.ListView):
    templates_name = "website/shop"

class CartView(generic.DetailView):
    template_name = "website/cart"

class OtherView(generic.DetailView):
    template_name = "website/other"