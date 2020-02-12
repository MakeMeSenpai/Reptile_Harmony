from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

#pulls from our models
from website.models import Home

# Create your views here.
class index(generic.DetailView):
    model = Home
    template_name = 'website/index.html'

    def get_queryset(self):
        return Home.objects.filter(
            pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def shop(request):
    return render(request, 'website/shop.html')

def cart(request):
    return render(request, 'website/cart.html')

def other(request):
    return render(request, 'website/other.html')