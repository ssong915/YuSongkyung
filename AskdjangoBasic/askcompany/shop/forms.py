from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__' #모델의 모든 필드가 가져와짐