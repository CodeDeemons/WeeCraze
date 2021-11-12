from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Vehicle

class VehicleForm(ModelForm):
    def __init__(self, *args, **kwargs):
            kwargs.setdefault('label_suffix', '')
            super(VehicleForm, self).__init__(*args, **kwargs)

    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    model = forms.CharField(label='Model', widget=forms.TextInput(attrs={'class':'form-control'}))
    brand = forms.CharField(label='Brand', widget=forms.TextInput(attrs={'class':'form-control'}))
    milleage = forms.CharField(label='Milleage', widget=forms.NumberInput(attrs={'class':'form-control'}))
    cc = forms.CharField(label='Cubic Capacity', widget=forms.NumberInput(attrs={'class':'form-control'}))
    type = forms.CharField(label='Type', widget=forms.TextInput(attrs={'class':'form-control'}))
    desc = forms.CharField(label='Info', widget=forms.Textarea(attrs={'cols':63, 'rows':5, 'class':'form-control'}))
    img_name = forms.CharField(label='Image Name', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Vehicle
        fields = ['name', 'model', 'brand', 'milleage', 'cc', 'type', 'img_name', 'desc']