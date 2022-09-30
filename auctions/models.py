from email.mime import image
from unicodedata import name
from django.db import models
from django.forms import CharField
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
    image = models.ImageField('image', upload_to="category_imgs/")

    def __str__(self) -> str:
        return f"{self.id} {self.name}"

class Post(models.Model):
    user = models.ForeignKey(CustomUser,models.CASCADE,related_name="posts")
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    model = models.IntegerField()
    color = models.CharField(max_length=40)
    discription = models.TextField()
    categories = models.ForeignKey(Category,models.CASCADE,related_name="posts")
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.id} {self.name}"

class Location(models.Model):
    user = models.ForeignKey(CustomUser,models.CASCADE,related_name="locations")
    name = models.CharField(max_length=40)
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self) -> str:
        return f"{self.id} {self.name}"

class Favorite(models.Model):
    user = models.ForeignKey(CustomUser,models.CASCADE,related_name="favs")
    post = models.ForeignKey(Post,models.CASCADE,related_name="favs")

    def __str__(self) -> str:
        return f"{self.id} {self.post}"

class Comment(models.Model):
    user = models.ForeignKey(CustomUser,models.CASCADE,related_name="comments")
    comment = models.TextField()
    post = models.ForeignKey(Post,models.CASCADE,related_name="comments")

    def __str__(self) -> str:
        return f"{self.post}"

class PostImages(models.Model):
    image = models.ImageField('image', upload_to="post_imgs/")
    post = models.ForeignKey(Post,models.CASCADE,related_name="images")

    def __str__(self) -> str:
        return f"{self.id} {self.post}"