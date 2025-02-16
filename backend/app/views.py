from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "name": "John",
        "age": 23,
        "nationalities": ["American", "Canadian"]
    }

    return render(request,"index.html", context)
    # return render(request,"index.html", {"context":context})
    # return HttpResponse("hello world")
