from django import forms
from .models import *


class FormComment(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = [""]
        fields = {"name", "comment"}
        widgets = {
            "comment": forms.Textarea(attrs={
                'placeholder': 'Ваш комментарий',
                'required': '',
                'rows': '8'})
        }


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'email', 'message']
        exclude = [""]
        widgets = {
            "comment": forms.Textarea(attrs={
                'placeholder': 'Оставьте сообщение...',
                'required': '',
                'rows': '8'})
        }


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['name', 'last_name', 'message']
        exclude = [""]
        widgets = {
            "comment": forms.Textarea(attrs={
                'placeholder': 'Оставьте ваш отзыв',
                'required': '',
                'rows': '8'})
        }