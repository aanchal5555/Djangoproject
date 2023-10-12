from django.contrib import admin
from django.db import models  # Use this import statement

from productcart.models import Products, Category, Subcategory

# Rest of your admin.py code remains the same

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_desc', 'product_price', 'product_image', 'showcase_badge', 'showcase_rating', 'discounted_price', 'category', 'subcategory')

admin.site.register(Products, ProductAdmin)
admin.site.register(Category)  # Register the Category model
admin.site.register(Subcategory)  # Register the Subcategory model





