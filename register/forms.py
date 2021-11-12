from django import forms
from django.contrib.auth.forms import UserCreationForm
from register.models import Client

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
            kwargs.setdefault('label_suffix', '')
            super(RegisterForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=30, help_text="Must be unique")
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}), help_text="Enter valid Email")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), help_text='Enter First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), help_text='Enter Last Name')
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label='Age', max_value=90, required=True,)
    contact = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), error_messages={'contact':'Enter valid contact'})
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password', help_text="Includes no. and letters(minimum 8 chars)")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Confirm Password', help_text= 'Must be match')

    class Meta:
        model = Client
        fields = ['username', 'email', 'first_name', 'last_name', 'age', 'contact', 'password1', 'password2']