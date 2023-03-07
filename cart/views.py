from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)
    #如果用戶登入
    if current_user.is_authenticated:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except:
            pass
        try:
            cart_item = CartItem.objects.get(product=product, user=current_user)
            cart_item.quantity += 1
            cart_item.save()
        except:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                user = current_user,
            )
            cart_item.save()
        return redirect('cart')
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except:
            cart = Cart.objects.create(
                cart_id = _cart_id(request)
            )
        cart.save()
        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        except:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart,
            )
            cart_item.save()
        return redirect('cart')

def delete_cart(requset, product_id):
    product = Product.objects.get(id=product_id)
    try:
        if requset.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=requset.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(requset))
            cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')

def delete_cart_item(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=request.user)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, active=True)
        for item in cart_items:
            total += (item.product.price * item.quantity)
            quantity += item.quantity
    except:
        pass
    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items
    }
    return render(request, 'store/cart.html', context)

@login_required(login_url="login")
def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(crat=cart, active=True)
        for item in cart_items:
            total += (item.product.price * item.quantity)
            quantity += item.quantity
    except:
        pass
    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items
    }
    return render(request, 'store/checkout.html', context)