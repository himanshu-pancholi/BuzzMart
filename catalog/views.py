from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def shop(request):
    return render(request, 'shop.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def wheat(request):
    return render(request, 'wheat.html')

def product(request):
    return render(request, 'product.html')

def vegetables(request):
    return render(request, 'vegetables.html')
def spicies(request):
    return render(request, 'spicies.html')

def fruits(request):
    return render(request, 'fruits.html')

def dairy(request):
    return render(request, 'dairy.html')