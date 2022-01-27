from django.urls import path

from admins.views import index, UsersListView, UsersCreateView, UsersUpdateView, UsersDeleteView, \
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, \
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, OrderListView, OrderUpdateView, \
    StoresListView, StoresCreateView, StoresUpdateView, StoresDeleteView

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),

    path('users/', UsersListView.as_view(), name='admin_users'),
    path('users-create/', UsersCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UsersUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UsersDeleteView.as_view(), name='admin_users_delete'),

    path('categories/', CategoryListView.as_view(), name='admin_category'),
    path('categories-create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('categories-update/<int:pk>', CategoryUpdateView.as_view(), name='admin_category_update'),
    path('categories-delete/<int:pk>', CategoryDeleteView.as_view(), name='admin_category_delete'),

    path('products/', ProductListView.as_view(), name='admin_products'),
    path('products-create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('products-update/<int:pk>', ProductUpdateView.as_view(), name='admin_products_update'),
    path('products-delete/<int:pk>', ProductDeleteView.as_view(), name='admin_products_delete'),

    path('orders/', OrderListView.as_view(), name='admin_orders'),
    path('orders-update/<int:pk>', OrderUpdateView.as_view(), name='admin_orders_update'),

    path('stores/', StoresListView.as_view(), name='admin_stores'),
    path('stores-create/', StoresCreateView.as_view(), name='admin_stores_create'),
    path('stores-update/<int:pk>', StoresUpdateView.as_view(), name='admin_stores_update'),
    path('stores-delete/<int:pk>', StoresDeleteView.as_view(), name='admin_stores_delete'),

]
