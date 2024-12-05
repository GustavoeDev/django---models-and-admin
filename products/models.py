from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=200, decimal_places=2)
    quantity = models.IntegerField()
    createdAt = models.DateTimeField()
