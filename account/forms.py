from django import forms
from .models import UID

class UIDForm(forms.ModelForm):
    class Meta:
        model = UID
        fields = ['UID']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'UID'
            })
        }