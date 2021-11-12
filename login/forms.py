from register.models import Client
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
            kwargs.setdefault('label_suffix', '')
            super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Username', max_length=30, help_text="We don't share any of your info")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password')

    class Meta:
        model = Client
        fields = ['username', 'password']