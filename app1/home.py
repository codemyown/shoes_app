from django.db import models



class Home(models.Model):
    product_name = models.CharField(max_length = 50)
    more_name = models.CharField(max_length = 50)
    description = models.TextField()
    shoes_image = models.ImageField(upload_to = "upload/images")
    image2 = models.ImageField(upload_to = "upload/images")
    
    
    def __str__(self):
        return self.product_name
    
    
    def get_all_home_products():
        return Home.objects.all()
    
    