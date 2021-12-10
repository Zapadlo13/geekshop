from django.urls import path
from mainapp.views import products,detail


app_name = 'products'
urlpatterns = [

    path('', products, name='products'),
    path('category/<int:id_category>/', products, name='category'),
    path('page/<int:page>/', products, name='page'),
    path('detail/<int:id>/', detail, name='detail'),

]
