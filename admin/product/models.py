# models.py

from djongo import models

class Product(models.Model):
    product_id = models.CharField(max_length=50, unique=True,null=False,blank=False)
    product_name = models.CharField(max_length=255,null=False,blank=False)
    description = models.TextField()
    quantity = models.IntegerField()
    ratings = models.FloatField()
    price = models.FloatField(null=False,blank=False)