from django import views
from django.urls import path, include
from . import views

urlpatterns = [
   path('',views.index,name="index"),
   path("login", views.login_view, name="login"),
   path("logout", views.logout_view, name="logout"),
   path("register", views.register, name="register"),
   path("newpost",views.newpost,name="newpost"),
   path("save",views.save,name="save"),
   path('display/<int:item_id>', views.display,name='display'),
   path('favorite',views.favorite,name="favorite"),
   path('favcreate/<int:item_id>',views.favcreate,name="favcreate")
]
