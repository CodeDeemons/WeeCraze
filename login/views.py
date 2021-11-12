from django.http.response import HttpResponseRedirect
from login.forms import LoginForm
from django.contrib.auth import login as authlogin, authenticate, logout
from django.contrib import messages
from django.shortcuts import render

# Create your views here.

def login(request):
	if request.POST:
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				if user.is_superuser:
					authlogin(request, user)
					messages.info(request, f"You are now logged in as Superuser {username}.")
					return HttpResponseRedirect('/', {'home' : 'active'})
				else:
					authlogin(request, user)
					messages.info(request, f"You are now logged in as {username}.")
					return HttpResponseRedirect('/booking/destiny/', {'destiny' : 'active'})
		else:
			form = LoginForm()
			messages.warning(request,"Invalid username or password.")
	form = LoginForm()
	context = {'login' : 'active', 'fm' : form}
	return render(request, 'login/login.html', context)

def logout_request(request):
	logout(request)
	messages.info(request, "You are successfully logged out.") 
	return HttpResponseRedirect('/', {'home' : 'active'})