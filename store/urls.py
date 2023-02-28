from django.urls import path
from . import views
urlpatterns = [
    path('', views.store, name="store"),
    path('<slug:slug>/', views.store),
    path('<slug:slug>/<slug:product_slug>', views.product_detail, name="product_detail"),
]