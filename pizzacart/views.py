from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Product
# Create your views here.

def home(request):
    products = Product.objects.all()
    thumb_items = {'product': products}
    return render(request, 'pizzacart/home.html', thumb_items)
    

def index(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}

    products = Product.objects.all()
    thumb_items = {'product': products} #thumbnail items to display on homepage

    #creating cart using sessions
    if request.method == 'POST':
        pizitem = request.POST.get('pizitem')
        decrease = request.POST.get('minus')
        cart = request.session.get('cart')
        if cart:
            number = cart.get(pizitem)
            if number:
                if decrease:
                    if number <= 1:
                        cart.pop(pizitem)
                    else:
                        cart[pizitem] = number - 1
                else:
                    cart[pizitem] = number + 1
            else:
                cart[pizitem] = 1
        else:
            cart = {}
            cart[pizitem] = 1

        request.session['cart'] = cart
        print("Cart:", request.session['cart'])
        return redirect('/pizzacart')

    return render(request, 'pizzacart/index.html', thumb_items)

    
def contact(request):
    return render(request, 'pizzacart/contact.html')

def about(request):
    return render(request, 'pizzacart/about.html')

def view_pizza(request, eid):
    product = Product.objects.filter(eid=eid)
    
    return render(request, 'pizzacart/pizView.html',{'pizza':product[0]})

def checkout(request):
    return render(request, 'pizzacart/checkout.html')

def pizzacart(request):
    eids = list(request.session.get('cart').keys())
    items = Product.get_product(eids)
    print(items)
    product = {'items': items}
    return render(request, 'pizzacart/pizcart.html', product)