from django.contrib import messages
from django.http.response import HttpResponseRedirect
from destiny.forms import DestinyForm
from django.shortcuts import redirect, render
from .models import Destiny

# Create your views here.

def destiny(request):
    dest = Destiny.objects.all()
    context = {'booking' : 'active', 'destiny' : 'active', 'destiny_show' : dest}
    return render(request, 'destiny/destiny.html', context)

def add_dest(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = DestinyForm(request.POST)
            if form.is_valid():
                Destiny = form.save()
                name = Destiny.name
                messages.success(request, name + '.. New Destination has been added.')
                return HttpResponseRedirect('/booking/destiny/', {'destiny' : 'active'})

        else:
            form = DestinyForm()

    context = { 'destiny' : 'active', 'fm' : DestinyForm}
    return render(request, 'destiny/add_dest.html', context)

def dest_info(request, dest_name):
    dest_more = Destiny.objects.get(name=dest_name)
    context = {'booking' : 'active', 'destiny' : 'active', 'dest_more' : dest_more}
    return render(request, 'destiny/dest_info.html', context)

def delete_dest(request, dest_id):
    destiny = Destiny.objects.get(id = dest_id)
    destiny.delete()
    messages.success(request, 'Destiny Successfully Deleted')
    return HttpResponseRedirect('/booking/destiny/', {'destiny' : 'active'})