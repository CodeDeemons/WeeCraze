from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You registered successfully.. ')
            return HttpResponseRedirect('/login/', {'login' : 'active'})

        messages.warning(request, 'Sorry.. Failed to register, Fill details carefully')
            
    form = RegisterForm()

    context = { 'register' : 'active', 'fm' : form}
    return render(request, 'register/register.html', context)