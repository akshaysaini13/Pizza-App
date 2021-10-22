from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    thumb_items = {'product': products} #thumbnail items to display on homepage
    return render(request, 'pizzacart/index.html', thumb_items)

def contact(request):
    return render(request, 'pizzacart/index.html')

def about(request):
    return render(request, 'pizzacart/about.html')

def view_pizza(request):
    return render(request, 'pizzacart/index.html')

def checkout(request):
    return render(request, 'pizzacart/index.html')