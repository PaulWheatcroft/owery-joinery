from django.contrib import admin
from .models import Product, Category, Style

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'style',
        'price',
    )

    ordering = ('category', 'style')


admin.site.register(Category)
admin.site.register(Style)
admin.site.register(Product, ProductAdmin)
