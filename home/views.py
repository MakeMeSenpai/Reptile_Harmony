# from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
# imports our database stuff
from .models import Home
myObj = Home.objects.get(id=1)
print("*****")
# print(myObj.img.url)
print("*****")


# Create your views here.
def home_view(request):
    content = {
        "content": myObj
    }
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", content)
