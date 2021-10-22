from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('contact/', views.contact, name="Contact Us"),
    path('about/', views.about, name="About"),
    path('viewpizza/', views.view_pizza, name="view Pizza"),
    path('checkout/', views.checkout, name="checkout")

]
