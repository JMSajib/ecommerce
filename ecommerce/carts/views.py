from django.shortcuts import render,redirect
from .models import Cart
from products.models import Product
# Create your views here.

def cart_page(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request,"carts/home_page.html",{"cart":cart_obj})

def cart_update(request):
    product_id=request.POST.get('product_id')
    print(product_id)
    if(product_id is not None):
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:home")

        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if(product_obj in cart_obj.products.all()):
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
    return redirect("cart:home")
