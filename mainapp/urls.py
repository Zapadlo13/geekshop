from django.urls import path
from mainapp.views import products,ProductDetail
from django.views.decorators.cache import cache_page

app_name = 'products'
urlpatterns = [

    path('', products, name='products'),
    path('category/<int:id_category>/', products, name='category'),
    path('page/<int:page>/', products, name='page'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),

]
