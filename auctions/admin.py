from django.contrib import admin
from .models import CustomUser, Profile, Category, Post, Location, Favorite,Comment,PostImages
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Location)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(PostImages)