from django.shortcuts import render
from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)


def detail(request,id):
    context = {
        'title': 'GeekShop - Продукт',
        'products': Product.objects.filter(id=id) ,
    }
    return render(request, 'mainapp/products.html', context)


