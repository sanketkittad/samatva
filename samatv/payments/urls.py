from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('donate',views.donate,name="donate"),
    path('contact',views.contact,name="contact"),
    path('success',views.success,name="success")
]