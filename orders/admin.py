from django.contrib import admin
from .models import Order



class CustomOrder(admin.ModelAdmin):
    search_fields= ['user']
    list_display = ('user','order_date','is_finished')
    list_filter  = ['order_date']


# Register your models here.
admin.site.register(Order, CustomOrder)

