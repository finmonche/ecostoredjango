from django.db import models
from store.models import Product
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_add = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "購物車"
        verbose_name_plural = "購物車"

    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="商品")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,verbose_name="購物車訂單")
    quantity = models.IntegerField(verbose_name="數量")
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "訂單"
        verbose_name_plural = "訂單"

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product