from django.contrib import admin
from .models import CustomUser, Profile, Category, Post, Location,Comment,PostImages,Model,Color,Brand,Mileage
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Location)

admin.site.register(Comment)
admin.site.register(PostImages)
admin.site.register(Model)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Mileage)
