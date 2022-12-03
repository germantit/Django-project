from django import forms
from .models import *


class SaleOrderForm(forms.ModelForm):

    class Meta:
        model = SaleOrder
        fields = ['name', 'phone', 'email', 'message']
        exclude = [""]
        widgets = {
            "comment": forms.Textarea(attrs={
                'placeholder': 'Оставьте сообщение...',
                'required': '',
                'rows': '8'})
        }
