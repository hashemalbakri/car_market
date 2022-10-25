from pyexpat import model
from unicodedata import category
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import  Brand, Contact, CustomUser, Mileage, Model, Profile, Category, Post, Location,Comment,PostImages,Color
from django.db import IntegrityError
import datetime
from django.db.models import Q
from django.core.paginator import Paginator

import json
from flask import request
from flask import Flask, render_template, jsonify
import sys
app = Flask(__name__)

from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize



# Create your views here.
def search(request):
    items = Post.objects.all()  
    colors = Color.objects.all()
    models = Model.objects.all()
    brands = Brand.objects.all()
    mileage = Mileage.objects.all()
    category = Category.objects.all()
    # items = items.filter(
    #     Q(brand__brand=request.GET.get('brand'))|
    #     Q(model__year=request.GET.get('model'))|
    #     Q(name__icontains=request.GET.get('name'))
    # )
    if request.GET.get('brand'):
        items = items.filter(brand__brand=request.GET.get('brand'))
    if request.GET.get('model'):
     items = items.filter(model__year=request.GET.get('model'))
    if request.GET.get('color'):
        items = items.filter(color__color=request.GET.get('color'))
    if request.GET.get('mileage'):
        items = items.filter(mileage__mileage=request.GET.get('mileage'))
    if request.GET.get('category'):
        items = items.filter(category__name=request.GET.get('category'))
    if request.GET.get('name'):
        items = items.filter(name__icontains=request.GET.get('name'))
    return render(request, "auctions/index.html",{
        "items":items,
        "colors":colors,
        "models":models,
        "brands":brands,
        "mileage":mileage,
        "category":category,
    })

def index(request):
    x = Post.objects.all().order_by('-time_create')
    p = Paginator(x,6)
    page = request.GET.get('page')
    posts = p.get_page(page)
    numbers = 's' * posts.paginator.num_pages
    colors = Color.objects.all()
    models = Model.objects.all()
    brands = Brand.objects.all()
    mileage = Mileage.objects.all()
    category = Category.objects.all()
    return render(request, "auctions/index.html",{
        "items":posts,
        'colors': colors,
        "models":models,
        "numbers": numbers,
        "brands":brands,
        "mileage":mileage,
        "category":category
    })

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

def shop(request):
    posts = Post.objects.all()
    return render(request,"auctions/shop.html",{
        "posts": posts,
    })


def newpost(request):
    brands = []
    brands = Brand.objects.all()
    models = []
    models = Model.objects.all()
    colors = []
    colors = Color.objects.all()
    category = []
    category = Category.objects.all()
    return render(request,"auctions/post.html",{
        "brands":brands,
        "models":models,
        "colors":colors,
        "category":category
    })

def save(request):
    if request.method == "POST":
        brand = request.POST["brand"]
        brand = Brand.objects.get(brand=brand)
        carName = request.POST["carName"]
        year = request.POST['model']
        model = Model.objects.get(year=year)
        color = request.POST["color"]
        colors = Color.objects.get(color=color)
        cate = request.POST['category']
        category = Category.objects.get(name=cate)
        phone = request.POST["phone"]
        facebook = request.POST["facebook"]
        description = request.POST["description"]
        price = request.POST["price"]
        image1 = request.FILES.getlist('image')
        user = request.user
        time = datetime.datetime.now()    
        content = Post.objects.create(
            brand = brand,
            name = carName,
            model = model,
            color = colors,
            categories = category,
            description = description,
            price = price,
            time_create = time,
            user = user,
            phoneNumber = phone,
            social = facebook,
        )

        for image in image1:
            PostImages.objects.create(
            post = content,
            image = image
        )
        item_id = content.pk
        return display(request,item_id)

def display(request,item_id):
    item = None
    user = None
    user = CustomUser.objects.filter(username = request.user)
    item = Post.objects.get(id = item_id) 
    owner = request.user
    listingInWatch = owner in item.watchList.all()
    allComments = Comment.objects.filter(post=item_id)
    postImages = PostImages.objects.filter(image=item_id)
    return render(request,"auctions/display.html",{
        "item":item,
        "user":user,
        "listingInWatch":listingInWatch,
        "allComments":allComments,
        "postImages": postImages,
    })
    
def watchList(request):
    fav = request.user.Watch.all()
    return render(request,'auctions/watchList.html',{
        'data': fav,
    })


def remove(request, id):
    data = Post.objects.get(pk=id)
    owner = request.user
    data.watchList.remove(owner)
    return HttpResponseRedirect(reverse("display", args=(id, )))

def add(request, id):
    data = Post.objects.get(pk=id)
    owner = request.user
    data.watchList.add(owner)
    return HttpResponseRedirect(reverse("display", args=(id, )))

def carwash(request):
    
    return render(request,'auctions/carwash.html')

@csrf_exempt
def getlocations(request):
    locations = Location.objects.all()
    return JsonResponse([location.serialize() for location in locations],safe=False)

def comment(request,id):
    posts = Post.objects.get(pk=id)
    owner = request.user
    message = request.POST['userComment']

    newComment = Comment(
        user = owner,
        post = posts,
        comment = message,
    )
    newComment.save()

    return HttpResponseRedirect(reverse('display', args=(id, )))

@csrf_exempt
def saveLoc(request):
    data = json.loads(request.body)
    print(data)
    x = data.get("lat","")
    y = data.get("long","")
    title = data.get("title","")
    content = Location(
        x = x,
        y = y,
        user = request.user,
        name = title,
    )
    content.save()
    return HttpResponse ("")
    
def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact.objects.create(
        name = name,
        email = email,
        message = message
        )
    return render(request,"auctions/contact.html")
