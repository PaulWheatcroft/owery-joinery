from django.contrib import admin
from .models import Product, Category, Style

# Register your models here.
admin.site.register(Category)
admin.site.register(Style)
admin.site.register(Product)
