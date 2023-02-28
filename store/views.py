from django.shortcuts import render,get_object_or_404
from .models import Product
from product.models import Category
# Create your views here.

def store(request, slug=None):
    category = None
    queryset = None
    if slug != None:
        category = Category.objects.filter(slug=slug).first()
        queryset = Product.objects.filter(category=category)
    else:
        queryset = Product.objects.all()

    categoryname = Category.objects.all()
    context = {
        "queryset":queryset,
        "category":category,
        "categoryname": categoryname,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, slug, product_slug):
    try:
        product = Product.objects.get(category__slug=slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        "product":product
    }
    return render(request, 'store/product_detail.html',context)