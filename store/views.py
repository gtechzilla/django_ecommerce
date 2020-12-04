from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'store_pages/home.html')

def checkout(request):
    return render(request,'store_pages/checkout.html')

def cart(request):
    return render(request,'store_pages/cart.html')