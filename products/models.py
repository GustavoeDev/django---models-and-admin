from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name
    
class Category(models.Model):
    name = models.CharField(max_length=200)  
    description = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True) 
      
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    quantity = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True) 
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True, related_name="products_category")

    def __str__(self):
        return self.name


