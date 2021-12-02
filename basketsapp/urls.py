from django.urls import path

from basketsapp.views import basket_add,basket_remove

app_name = 'basketsapp'
urlpatterns = [
    path('add/<int:id>/', basket_add, name='basket_add'),
    path('remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
