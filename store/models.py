from django.db import models
from product.models import Category
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="商品名稱")
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=255, blank=True, verbose_name="商品詳細")
    price = models.IntegerField(verbose_name="商品價格")
    image = models.ImageField(upload_to="photos/product", null=True, blank=True, verbose_name="商品圖片")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="商品分類")
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"
    
    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse("product_detail", args=[self.category.slug, self.slug])
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url