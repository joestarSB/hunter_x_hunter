from .models import Category, Gems
from django import forms

class GemsForm(forms.ModelForm):
    class Meta:
        model = Gems
        fields =['title', 'description', 'balance', 'category']

class BuyGemForm(forms.Form):
    card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'type':'number'}))
    data = forms.CharField(max_length=5)
    CVV = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'type':'number'}))
    name = forms.CharField(max_length=30)