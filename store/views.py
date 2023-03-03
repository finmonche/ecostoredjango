from django.shortcuts import render,get_object_or_404
from .models import Product
from product.models import Category
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.http import HttpResponse
# Create your views here.

def store(request, slug=None):
    category = None
    queryset = None
    if slug != None:
        category = Category.objects.filter(slug=slug).first()
        queryset = Product.objects.filter(category=category)
        paginator = Paginator(queryset, 3)
        page = request.GET.get('page', 1)
        paged_products = paginator.get_page(page)
    else:
        queryset = Product.objects.all()
        paginator = Paginator(queryset, 3)
        page = request.GET.get('page', 1)
        paged_products = paginator.get_page(page)
    categoryname = Category.objects.all()
    context = {
        "products":paged_products,
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

def searchkey(request):
    if "search" in request.GET:
        search = request.GET['search']
        if search:
            products = Product.objects.filter(description__icontains=search)
    context = {
        "products" : products
    }

    return render(request, 'store/store.html', context)