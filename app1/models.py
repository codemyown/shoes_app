from django.db import models


# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to = "upload/images")
    name = models.CharField(max_length = 50)
    price = models.IntegerField(default = 0)
    original_price = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name
    
    
    def get_all_products():
        return Product.objects.all()
    
