from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('offers/', views.offers, name='offers'),
    path('fragrance/', views.fragrance, name='fragrance'),
    
    # Cart & Checkout & Signup
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('signup/', views.signup_view, name='signup'),
    path('checkout/', views.checkout, name='checkout'),
]