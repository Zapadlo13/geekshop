from django import forms
from storesapp.models import Store


class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ('__all__')


