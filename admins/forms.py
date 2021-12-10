from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authapp.models import User
from mainapp.models import ProductCategory, Product


class UserAdminRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'image', 'first_name', 'last_name', 'username', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'image', 'first_name', 'last_name', 'username', 'age',)

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class CategoryAdminRegisterForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class CategoryAdminProfileForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ProductAdminRegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'image', 'short_desc', 'description', 'price', 'quantity')

    def __init__(self, *args, **kwargs):
        super(ProductAdminRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductAdminProfileForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'image', 'short_desc', 'description', 'price', 'quantity')

    def __init__(self, *args, **kwargs):
        super(ProductAdminProfileForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
