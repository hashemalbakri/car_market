
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
    image = models.ImageField('image', upload_to="category_imgs/")

    def __str__(self) -> str:
        return f"{self.id} {self.name}"

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

    def __str__(self) -> str:
        return f"{self.id}"   

class Post(models.Model):
    user = models.ForeignKey(CustomUser,models.CASCADE,related_name="posts")
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    model = models.ForeignKey(Model,models.CASCADE,related_name="posts")
    color = models.ForeignKey(Color,models.CASCADE,related_name="posts")
    description = models.TextField()
    categories = models.ForeignKey(Category,models.CASCADE,related_name="posts",null=True)
    image = models.ForeignKey(PostImages,models.CASCADE,related_name="posts",null=True)
    price = models.FloatField()
    time_create = models.DateTimeField(null=True)

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
        