from django import forms
from .models import *


class BuyOrderForm(forms.ModelForm):

    class Meta:
        model = BuyOrder
        fields = ['name', 'phone']
        exclude = [""]
