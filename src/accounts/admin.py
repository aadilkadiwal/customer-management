from re import search
from django.contrib import admin
from .models import (
    Customer,
    Tag,
    Product,
    Order
)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',)
    search_fields = ('name', 'phone', 'email',)
admin.site.register(Customer, CustomerAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)     
admin.site.register(Tag, TagAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'price',)
    list_filter = ('category', 'tags',)
    search_fields = ('name',)
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'status',)
    list_filter = ('status',)
    search_fields = ('customer', 'product',)
admin.site.register(Order, OrderAdmin)