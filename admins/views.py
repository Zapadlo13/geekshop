from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminRegisterForm, \
    CategoryAdminProfileForm, ProductAdminRegisterForm, ProductAdminProfileForm
from authapp.models import User
from mainapp.mixin import UserDispatchMixin, BaseClassContextMixin
from mainapp.models import ProductCategory, Product


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
    form_class = UserAdminProfileForm
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


class CategoryDeleteView(DeleteView, UserDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_category')


@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'title': 'GeekShop - Admin |Список товаров ',
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-product-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminRegisterForm()

    context = {
        'title': 'GeekShop - Admin |Новый товар',
        'form': form
    }
    return render(request, 'admins/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, pk):
    select_product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProductAdminProfileForm(instance=select_product, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminProfileForm(instance=select_product)

    context = {
        'title': 'GeekShop - Admin |' + select_product.name,
        'form': form,
        'select_product': select_product
    }
    return render(request, 'admins/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, pk):
    if request.method == 'POST':
        select_product = Product.objects.get(pk=pk)
        select_product.delete()
    return HttpResponseRedirect(reverse('admins:admin_products'))
