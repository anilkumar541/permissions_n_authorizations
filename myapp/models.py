from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=99)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):    
        return self.category_name


class Product(models.Model):        
    product_name= models.CharField(max_length=99)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.product_name    
        