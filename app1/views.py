from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .features import Features
from .home import Home

# Create your views here.



def index(request):
    data1  = Product.get_all_products()
    data2 = Features.get_all_feature()
    data3 = Home.get_all_home_products()
    data = {
        'product':data1,
        'feature':data2,
        'home_image':data3
    }
    
    
    
    return render(request,"index.html",data)
