from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from django.urls import reverse

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminRegisterForm, \
    CategoryAdminProfileForm, ProductAdminRegisterForm, ProductAdminProfileForm
from authapp.models import User
from mainapp.models import ProductCategory, Product

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {
        'title': 'GeekShop - Admin ',

    }
    return render(request, 'admins/admin.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'title': 'GeekShop - Admin |Список пользователей ',
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()

    context = {
        'title': 'GeekShop - Admin |Новый пользователь  ',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, pk):
    user_select = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=user_select, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)

    context = {
        'title': 'GeekShop - Admin |' + user_select.username,
        'form': form,
        'user_select': user_select

    }
    return render(request, 'admins/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))

@user_passes_test(lambda u: u.is_superuser)
def admin_category(request):
    context = {
        'title': 'GeekShop - Admin |Список категорий ',
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-category-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryAdminRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
    else:
        form = CategoryAdminRegisterForm()

    context = {
        'title': 'GeekShop - Admin |Новая категория',
        'form': form
    }
    return render(request, 'admins/admin-category-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, pk):

    select_category = ProductCategory.objects.get(pk=pk)

    if request.method == 'POST':
        form = CategoryAdminProfileForm(instance=select_category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
    else:
        form = CategoryAdminProfileForm(instance=select_category)

    context = {
        'title': 'GeekShop - Admin |' + select_category.name,
        'form': form,
        'select_category': select_category
    }
    return render(request, 'admins/admin-category-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, pk):
    if request.method == 'POST':
        select_categogy = ProductCategory.objects.get(pk=pk)
        select_categogy.delete()
    return HttpResponseRedirect(reverse('admins:admin_category'))

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
        form = ProductAdminRegisterForm(data=request.POST,files=request.FILES)
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
        form = ProductAdminProfileForm(instance=select_product, data=request.POST,files=request.FILES)
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
