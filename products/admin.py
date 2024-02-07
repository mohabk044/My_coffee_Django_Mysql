from django.contrib import admin
from .models import Product


class CustomProduct(admin.ModelAdmin):
    search_fields= ['name']
    list_display = ('name','description','price','is_active')
    list_filter  = ['price']
# Register your models here.
admin.site.register(Product, CustomProduct)

