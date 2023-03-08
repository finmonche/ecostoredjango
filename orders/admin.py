from django.contrib import admin
from .models import Paymenet, Order, OrderProduct
# Register your models here.

admin.site.register(Paymenet)
admin.site.register(Order)
admin.site.register(OrderProduct)