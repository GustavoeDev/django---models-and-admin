from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_products, name='product_list'),
    path('details/<int:code>', views.view_details_product, name='details_product')
]