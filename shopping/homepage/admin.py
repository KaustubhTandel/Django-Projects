from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock_quantity', 'is_featured']
    list_filter = ['category', 'is_featured', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_featured', 'stock_quantity']