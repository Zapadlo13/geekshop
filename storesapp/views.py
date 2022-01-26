from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from geekshop.settings import EASY_MAPS_GOOGLE_KEY
from mainapp.mixin import BaseClassContextMixin
from storesapp.models import Store


class StoresList(ListView, BaseClassContextMixin):
    model = Store
    title = 'GeekShop | Список пунктов выдачи'
    template_name = 'storeapp/store_list.html'

    def get_queryset(self):
        return Store.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super(StoresList, self).get_context_data(**kwargs)
        context['EASY_MAPS_GOOGLE_KEY'] = EASY_MAPS_GOOGLE_KEY
        return context
