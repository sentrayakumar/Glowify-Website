from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    
    return render(request, 'shop.html', {'products': products})

def offers(request):
    return render(request, 'offers.html')

def fragrance(request):
    return render(request, 'frangrance.html')

from django.shortcuts import redirect, get_object_or_404
from .models import Product, CartItem


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')


def view_cart(request):
    cart_items = CartItem.objects.all()
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# (Signup)
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Checkout 
def checkout(request):
    cart_items = CartItem.objects.all()
    total = sum(item.total_price() for item in cart_items)
    if request.method == 'POST':
        
        CartItem.objects.all().delete() 
        return render(request, 'order_success.html')
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total})