from django.contrib.auth.decorators import user_passes_test
from django.db.models import F
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminRegisterForm, \
    CategoryAdminProfileForm, ProductAdminRegisterForm, ProductAdminProfileForm, OrderAdminProfileForm, \
    OrderItemAdminProfileForm, StoreAdminRegisterForm
from authapp.models import User
from mainapp.mixin import UserDispatchMixin, BaseClassContextMixin
from mainapp.models import ProductCategory, Product
from ordersapp.models import Order, OrderItem
from storesapp.models import Store


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {
        'title': 'GeekShop - Admin ',

    }
    return render(request, 'admins/admin.html', context)


# Users
class UsersListView(ListView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'GeekShop - Admin |Список пользователей'


class UsersCreateView(CreateView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'GeekShop - Admin |Новый пользователь'


class UsersUpdateView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'GeekShop - Admin |Обновление данных'


class UsersDeleteView(DeleteView, UserDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()

        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()

        return HttpResponseRedirect(reverse('admins:admin_users'))


# Categories
class CategoryListView(ListView, BaseClassContextMixin, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'
    title = 'GeekShop - Admin |Список категорий '


class CategoryCreateView(CreateView, BaseClassContextMixin, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    form_class = CategoryAdminRegisterForm
    success_url = reverse_lazy('admins:admin_category')
    title = 'GeekShop - Admin |Новая категория'


class CategoryUpdateView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = CategoryAdminProfileForm
    success_url = reverse_lazy('admins:admin_category')
    title = 'GeekShop - Admin |Обновление данных'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        discount = int(request.POST.get('discount'))
        if self.object.discount != discount:
            self.object.product_set.update(discount=discount)
            self.object.product_set.update(price_discount=F('price') * (1 - discount / 100))
        return super(CategoryUpdateView, self).post(request, **kwargs)




class CategoryDeleteView(DeleteView, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_category')

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()

        if self.object.is_active:
            self.object.is_active = False
            self.object.product_set.update(is_active =False)
        else:
            self.object.is_active = True
            self.object.product_set.update(is_active=True)
        self.object.save()

        return HttpResponseRedirect(reverse('admins:admin_category'))

# Products
class ProductListView(ListView, BaseClassContextMixin, UserDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-read.html'
    title = 'GeekShop - Admin |Список товаров '


class ProductCreateView(CreateView, BaseClassContextMixin, UserDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-create.html'
    form_class = ProductAdminRegisterForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'GeekShop - Admin |Новый товар'


class ProductUpdateView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    form_class = ProductAdminProfileForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'GeekShop - Admin |Обновление данных'


class ProductDeleteView(DeleteView, UserDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    form_class = ProductAdminProfileForm
    success_url = reverse_lazy('admins:admin_products')

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()

        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()

        return HttpResponseRedirect(reverse('admins:admin_products'))

class OrderListView(ListView, BaseClassContextMixin, UserDispatchMixin):
    model = Order
    template_name = 'admins/admin-order-read.html'
    title = 'GeekShop - Admin |Список заказов'


class OrderUpdateView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = Order
    template_name = 'admins/admin-order-update-delete.html'
    form_class = OrderAdminProfileForm
    success_url = reverse_lazy('admins:admin_orders')
    title = 'GeekShop - Admin |Обновление данных'

    # def get_context_data(self, **kwargs):
    #     context = super(OrderUpdateView, self).get_context_data(**kwargs)
    #     context['orderitem'] = OrderItemAdminProfileForm(instance=OrderItem.objects.filter(order_id=self.object.pk))
    #     return context



# Stores
class StoresListView(ListView, BaseClassContextMixin, UserDispatchMixin):
    model = Store
    template_name = 'admins/admin-stores-read.html'
    title = 'GeekShop - Admin |Список пунктов выдачи'


class StoresCreateView(CreateView, BaseClassContextMixin, UserDispatchMixin):
    model = Store
    template_name = 'admins/admin-stores-create.html'
    form_class = StoreAdminRegisterForm
    success_url = reverse_lazy('admins:admin_stores')
    title = 'GeekShop - Admin |Новый пункт выдачи'


class StoresUpdateView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = Store
    template_name = 'admins/admin-stores-update-delete.html'
    form_class = StoreAdminRegisterForm
    success_url = reverse_lazy('admins:admin_stores')
    title = 'GeekShop - Admin |Обновление данных'


class StoresDeleteView(DeleteView, UserDispatchMixin):
    model = Store
    template_name = 'admins/admin-stores-update-delete.html'
    success_url = reverse_lazy('admins:admin_stores')

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()

        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()

        return HttpResponseRedirect(reverse('admins:admin_stores'))

