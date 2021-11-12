from django.contrib import messages
from register.models import Client
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
def home(request):
    context = {'home' : 'active'}
    return render(request, 'home/home.html', context)

def clients(request):
    clients_data = Client.objects.all()
    context = {'clients' : 'active', 'clients_data':clients_data}
    return render(request, 'home/clients.html', context)

def delete_client(request, client_id):
    client = Client.objects.get(id = client_id)
    client.delete()
    messages.success(request, 'Client Successfully Deleted')
    return HttpResponseRedirect('/clients/', {'client' : 'active'})