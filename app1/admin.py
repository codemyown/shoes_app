from django.contrib import admin
from .models import Product
from .features import Features
from .home import Home
# Register your models here.


admin.site.register(Product)
admin.site.register(Features)
admin.site.register(Home)








