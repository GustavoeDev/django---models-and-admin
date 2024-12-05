from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'createdAt'] 
    search_fields = ['codigo', 'nome']
    list_filter = ['createdAt']
    ordering = ['-createdAt']  
    
admin.site.register(Product, ProductAdmin)  