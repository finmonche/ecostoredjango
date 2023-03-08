import json
from datetime import datetime
from random import randint
from django.shortcuts import render, redirect
from cart.models import CartItem
from .models import Order
from .forms import OrderForm
# Create your views here.

def payments(request):
    body = json.loads(request.body)
    print(body)
    return render(request, 'orders/payments.html')


def place_order(request):
    user = request.user
    cart_item = CartItem.objects.filter(user=user)
    total = 0
    quantity=0
    for item in cart_item:
        total += (item.product.price * item.quantity)
        quantity += item.quantity
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        code = request.POST.get('code')
        order_number = datetime.now().strftime("%Y%m%d%H%M%S") + str(randint(1000, 9999))
        data = Order.objects.create(username=username, email=email, 
                                    phone=phone, code=code, user=user,
                                    address=address, order_number=order_number)
        data.save()

        order = Order.objects.get(user=user, order_number=order_number)
        context = {
            'order': order,
            "cart_item" : cart_item,
            "total" : total
        }
        return render(request, 'orders/payments.html', context)
    else:
        return redirect('checkout')