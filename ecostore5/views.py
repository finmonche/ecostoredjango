from django.shortcuts import render
from store.models import Product
def home(request):
    queryset = Product.objects.all()
    context = {
            "queryset":queryset,
            }
    return render(request, 'home.html', context)