from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def shop(request):
    return render(request, 'website/shop.html')

def cart(request):
    return render(request, 'website/cart.html')

def other(request):
    return render(request, 'website/other.html')