from django.urls import path
from .views import home, shop, contact, about, wheat, product, vegetables, spicies, fruits, dairy
urlpatterns = [
    path('', home, name='home'),
    path('home.html', home, name='home'),
    path('shop.html', shop, name='shop'),
    path('contact.html', contact, name='contact'),
    path('about.html', about, name='about'),
    path('wheat.html', wheat, name='wheat'),
    path('product.html', product, name='product'),
    path('vegetables.html', vegetables, name='vegetables'),
    path('spicies.html', spicies, name='spicies'),
    path('fruits.html', fruits, name='fruits'),
    path('dairy.html', fruits, name='dairy'),



]