from django.shortcuts import render
from django.views.generic import DetailView
from django.db.models import Count, Q
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page, never_cache



def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategory.objects.filter(product__is_active=True).distinct()
            cache.set(key,link_category)
        return link_category
    else:
        return  ProductCategory.objects.filter(product__is_active=True).distinct()

def get_link_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Product.objects.filter(is_active= True).select_related('category')
            cache.set(key,link_product)
        return link_product
    else:
        return Product.objects.filter(is_active= True).select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = Product.objects.get(id=pk)
            cache.set(key,product)
        return product
    else:
        return Product.objects.get(id=pk)

# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
        'products': Product.objects.filter(is_active= True).select_related('category') ,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id_category=None, page=1):
    if id_category:
        products = Product.objects.filter(category_id=id_category, is_active= True).select_related('category')
    else:
        products = Product.objects.filter(is_active= True).select_related('category')

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
        'categories': get_link_category(),
    }

    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['product'] = get_product(self.kwargs.get("pk"))
        return context
