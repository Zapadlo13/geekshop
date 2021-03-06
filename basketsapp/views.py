from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.template.loader import render_to_string

from basketsapp.models import Basket
from mainapp.models import Product


@login_required
def basket_add(request, id):
    user_select = request.user
    product = Product.objects.get(id=id)
    baskets = Basket.objects.filter(user=user_select, product=product)

    if baskets:
        basket = baskets.first()
        basket.quantity = F('quantity')+1
        basket.save()
    else:
        Basket.objects.create(user=user_select, product=product, quantity=1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, basket_id):
    Basket.objects.get(id=basket_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, basket_id, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(id=basket_id)

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        baskets = Basket.objects.filter(user=request.user). \
            order_by('product__category')

        content = {
            'baskets': baskets,
        }

        result = render_to_string('basketsapp/basket.html', content)

        return JsonResponse({'result': result})
