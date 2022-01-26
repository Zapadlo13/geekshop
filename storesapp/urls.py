from django.urls import path

from storesapp.views import StoresList

app_name = 'storesapp'
urlpatterns = [
    path('', StoresList.as_view(), name='stores_list'),

]
