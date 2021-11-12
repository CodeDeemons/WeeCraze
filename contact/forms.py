from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Contact

class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
            kwargs.setdefault('label_suffix', '')
            super(ContactForm, self).__init__(*args, **kwargs)

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    contact = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    adress = forms.CharField(widget=forms.Textarea(attrs={'cols':63, 'rows':7, 'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'cols':63, 'rows':7, 'class':'form-control'}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'contact', 'subject', 'adress', 'message']