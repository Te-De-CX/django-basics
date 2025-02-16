from django.shortcuts import render,redirect
from .models import Feature 
from django.contrib.auth.models import User, auth
from django.contrib import messages


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

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        
        if password == password2:
            if password.isdigit() or password.isalpha() or len(password) < 8:   
                messages.info(request,"password should be alphanumeric and minimum 8 characters")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request,"email Taken")
                    return redirect("register")
                elif User.objects.filter(username=username).exists():
                    messages.info(request,"username Taken")
                    return redirect("register")
                else :
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    print("user created")
                    return redirect("login")
        else:
            messages.info(request,"password not matching")
            return redirect("register")
    else:
        return render(request,"register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def post(request, pk):
    return render(request, "post.html", {"pk":pk})
    
def counter(request):
    posts = [1, 2, 3, 4, 5]
    return render(request,"counter.html",{"posts":posts})