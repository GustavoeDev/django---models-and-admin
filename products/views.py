from django.shortcuts import render

from .models import Product

def view_products(request):
    products = Product.objects.all()

    context = {'products': products}

    return render(request, 'products.html', context)

def view_details_product(request, code):
    product = Product.objects.get(code=code)

    context = {'product': product}

    return render(request, 'product_details.html', context)
