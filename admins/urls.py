from django.urls import path

from admins.views import index, UsersListView, UsersCreateView, UsersUpdateView, UsersDeleteView, \
    CategoryListView,CategoryCreateView,CategoryUpdateView,CategoryDeleteView,\
    admin_products,admin_products_create,admin_products_update,admin_products_delete

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

    path('products/', admin_products, name='admin_products'),
    path('products-create/', admin_products_create, name='admin_products_create'),
    path('products-update/<int:pk>', admin_products_update, name='admin_products_update'),
    path('products-delete/<int:pk>', admin_products_delete, name='admin_products_delete'),

]
