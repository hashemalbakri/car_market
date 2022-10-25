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
   path("remove/<int:id>", views.remove, name="remove"),
   path("add/<int:id>", views.add, name="add"),
   path("watchList", views.watchList, name="watchList"),
   path("carwash",views.carwash,name="carwash"),
   path("comment/<int:id>", views.comment, name="comment"),
   path("search/", views.search, name="search"),
   path("contact/", views.contact, name="contact"),
]
