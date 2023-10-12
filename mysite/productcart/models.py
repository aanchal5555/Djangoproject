
from django.db import models
from tinymce.models import HTMLField

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
  
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name




class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc = HTMLField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    product_image = models.ImageField(upload_to="products/", max_length=250, null=True, default=None)
    showcase_badge = models.CharField(max_length=10, null=True, blank=True)
    showcase_rating = models.PositiveIntegerField(null=True, blank=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # ForeignKey to Category for the main category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # ForeignKey to Subcategory for subcategory
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.product_name


