# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# ctr + k + c: comment, ctr + k + u: uncomment
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_id = models.CharField(db_column='product_id', primary_key=True, max_length=10)  
    product_name = models.CharField(db_column='product_name', max_length=25)  
    product_image = models.CharField(db_column='product_image', max_length=500, blank=True)  
    company = models.CharField(max_length=25)
    product_description = models.TextField(db_column='product_description')  
    quantity_in_stock = models.IntegerField(db_column='quantity_in_stock')  
    sell_price = models.IntegerField(db_column='sell_price')  

    #class Meta stores information about model settings that are not used to create tables.
    class Meta:
        db_table = 'products'

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    Time = models.DateTimeField(auto_now_add=True)
    Content = models.TextField()

    class Meta:
        db_table = 'comment'

class Cart(models.Model):
    ord = models.AutoField(db_column='ord', primary_key=True)
    quantity = models.IntegerField(db_column='quantity')
    user = models.CharField(db_column='user', max_length=25)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, db_column='product_id')

    class Meta:
        db_table = 'cart'



