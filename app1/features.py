from django.db import models




class Features(models.Model):
    big_image = models.ImageField(upload_to = "upload/images")
    first_image = models.ImageField(upload_to = "upload/images")
    second_image = models.ImageField(upload_to = "upload/images")
    third_image = models.ImageField(upload_to = "upload/images")
    forth_image = models.ImageField(upload_to = "upload/images")
    name = models.CharField(max_length = 50)
    desc = models.TextField()
    price  = models.IntegerField(default = 0)
    original_price  = models.IntegerField(default = 0)
    
    
    def __str__(self):
        return self.name
    
    
    def get_all_feature():
        return Features.objects.all()
    
    