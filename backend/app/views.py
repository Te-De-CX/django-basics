from django.shortcuts import render
from .models import Feature 
# from django.http import HttpResponse

# Create your views here.

# def index(request):
#     context = {
#         "name": "John",
#         "age": 23,
#         "nationalities": ["American", "Canadian"]
#     }

#     return render(request,"index.html", context)
#     # return render(request,"index.html", {"context":context})
#     # return HttpResponse("hello world")
    


def index(request):
    features = Feature.objects.all()
    
    return render(request,"index.html",{"features":features})