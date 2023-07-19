from django.shortcuts import render
from .models import Products
from .resources import ProductResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
# Create your views here.\

def upload(request):
    if request.method == 'POST':
        product_resource = ProductResource
        dataset = Dataset()
        new_product = request.FILES['myfile']
        product =Products.objects.all()

        if not new_product.name.endswith('xlsx'):
            messages.info(request,'Sorry only Excel format are accepted')
            return render (request,"upload.html",context={"data":product})
    

        imported_data = dataset.load(new_product.read(),format='xlsx')
        for data in imported_data:
            value = Products(
                data[0],
                data[1],
                data[2],
                data[3]
        )
            value.save()
    product =Products.objects.all()
    return render (request,"upload.html",context={"data":product})