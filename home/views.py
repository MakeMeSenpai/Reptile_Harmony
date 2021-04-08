# from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
# imports our database stuff
from .models import Home
myObj = Home.objects.get(id=1)


# Create your views here.
def home_view(request):
    content = {
        "content": myObj
    }
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", content)


# This is from old file... wonder what it was for
# class index(generic.DetailView):
#     model = Home
#     template_name = 'website/index.html'

#     def get_queryset(self):
#         return Home.objects.filter(
#             pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
