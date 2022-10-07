from pyexpat import model
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import CustomUser, Model, Profile, Category, Post, Location, Favorite,Comment,PostImages,Color
from django.db import IntegrityError
import datetime


# Create your views here.

def index(request):
    return render(request,"auctions/index.html")






def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
       
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))




def register(request):
    if request.method == "POST":
      
        email = request.POST['email']
        username = request.POST["username"]
        password = request.POST["password"]
        
        # Ensure password matches confirmation
        
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = CustomUser.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def newpost(request):
    brands = []
    brands = Category.objects.all()
    models = []
    models = Model.objects.all()
    colors = []
    colors = Color.objects.all()
    return render(request,"auctions/post.html",{
        "brands":brands,
        "models":models,
        "colors":colors
    })

def save(request):
    if request == "POST":
        brand = request.POST["brand"]
        carName = request.POST["carName"]
        model = request.POST["model"]
        color = request.POST["color"]
        description = request.POST["description"]
        price = request.POST["price"]
        image = request.POST["image"]
        user = request.user
        time = datetime.datetime.now()

        content = Post.objects.create(user=user,categories=brand,name=carName,color=color,description=description,price=price,model=model,image=image,time_create=time)
        content.save()
        item_id = content.pk
        return display(request,item_id)

def display(request,item_id):
    item = None
    user = None
    user = CustomUser.objects.filter(username = request.user)
    item = Post.objects.get(id = item_id)
    return render(request,"auctions/display.html",{
        "item":item,
        "user":user
    })