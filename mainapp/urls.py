from django.db.migrations.state import _get_app_label_and_model_name
from django.urls import path
from mainapp.views import index,products

app_name  = 'products'

urlpatterns = [

    path('', products, name='products'),
]
