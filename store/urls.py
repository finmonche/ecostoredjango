from django.urls import path
from . import views
urlpatterns = [
    path('', views.store, name="store"),
    path('category/<slug:slug>/', views.store),
    path('category/<slug:slug>/<slug:product_slug>', views.product_detail, name="product_detail"),
    path('search/', views.searchkey, name="search"),
]
