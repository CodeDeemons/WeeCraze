from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Destiny

class DestinyForm(ModelForm):
    def __init__(self, *args, **kwargs):
           kwargs.setdefault('label_suffix', '')
           super(DestinyForm, self).__init__(*args, **kwargs)

    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(label='State', widget=forms.TextInput(attrs={'class':'form-control'}))
    img_name = forms.CharField(label='Image Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    category = forms.CharField(label='Category', widget=forms.TextInput(attrs={'class':'form-control'}))
    short_desc = forms.CharField(label='Short Info', widget=forms.Textarea(attrs={'cols':63, 'rows':7, 'class':'form-control'}))
    long_desc = forms.CharField(label='More Info', widget=forms.Textarea(attrs={'cols':63, 'rows':7, 'class':'form-control'}))

    class Meta:
        model = Destiny
        fields = ['name', 'state', 'img_name', 'category', 'short_desc', 'long_desc']