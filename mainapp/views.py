from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
        'products': Product.objects.all().select_related('category') ,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id_category=None, page=1):
    if id_category:
        products = Product.objects.filter(category_id=id_category)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'GeekShop - Каталог',
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'mainapp/products.html', context)


def detail(request, id):
    context = {
        'title': 'GeekShop - Продукт',
        'product': Product.objects.get(id=id),
    }
    return render(request, 'mainapp/detail.html', context)
