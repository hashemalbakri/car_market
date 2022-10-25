
from email.policy import default
from tkinter import CASCADE
from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
 pass

class Profile(models.Model):
    user = models.ForeignKey(CustomUser,models.CASCADE, related_name="profile")
    image = models.ImageField('image', upload_to="profile_imgs/")

    def __str__(self) -> str:
        return f"{self.id} {self.user.name}"

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f"{self.name}"

class Brand(models.Model):
    brand = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f"{self.brand}"

class Mileage(models.Model):
    mileage = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f"{self.mileage}"

class Model(models.Model):
    year = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.year}"  




class Color(models.Model):
    color = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f"{self.color}" 

class PostImages(models.Model):
    image = models.ImageField('image', upload_to="post_imgs/")
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, related_name="images")
    def __str__(self) -> str:
        return f"{self.id}"   

class Post(models.Model):
    user = models.ForeignKey(CustomUser,models.CASCADE,related_name="posts")
    name = models.CharField(max_length=40)
    brand = models.ForeignKey(Brand,models.CASCADE,related_name="posts",default = None)
    model = models.ForeignKey(Model,models.CASCADE,related_name="posts")
    color = models.ForeignKey(Color,models.CASCADE,related_name="posts")
    mileage = models.ForeignKey(Mileage,models.CASCADE,related_name="posts",null=True)
    description = models.TextField()
    categories = models.ForeignKey(Category,models.CASCADE,related_name="posts",null=True)
    price = models.FloatField()
    time_create = models.DateTimeField(null=True)
    watchList = models.ManyToManyField(CustomUser,blank=True,related_name="Watch")
    phoneNumber = models.IntegerField(default = None)
    social = models.CharField(max_length = 80 ,default = None)

    def __str__(self) -> str:
        return f"{self.id} {self.name}"

class Location(models.Model):
    user = models.ForeignKey(CustomUser,models.CASCADE,related_name="locations")
    name = models.CharField(max_length=40)
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self) -> str:
        return f"{self.id} {self.name}"



class Comment(models.Model):
    user = models.ForeignKey(CustomUser,models.CASCADE,related_name="comments")
    comment = models.TextField()
    post = models.ForeignKey(Post,models.CASCADE,related_name="comments")

    def __str__(self) -> str:
        return f"{self.user} commented on {self.post}"

class Contact(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField(max_length = 60)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"   