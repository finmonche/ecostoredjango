from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True, verbose_name="產品分類")
    slug = models.SlugField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', null=True, blank=True)

    class Meta:
        verbose_name = "產品分類"
        verbose_name_plural = "產品分類"
    def __str__(self):
        return self.category_name
