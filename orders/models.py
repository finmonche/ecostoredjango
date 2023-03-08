from django.db import models
from cart.models import Cart, CartItem
from accounts.models import Account
from store.models import Product
from django.core.validators import RegexValidator
# Create your models here.

class Paymenet(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id
    
class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Paymenet, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    status_choices =(
        (1,"新訂單"),
        (2, "完成訂單"),
        (3, "取消訂單")
    )
    status = models.CharField(max_length=10, choices=status_choices, default=1)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Paymenet, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
 