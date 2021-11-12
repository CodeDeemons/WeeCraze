from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from contact.models import Contact as ContactModal

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact = form.save()
            name = Contact.name
            messages.success(request, 'Received your message.. We will be back to you ' + name)

    else:
        # messages.warning(request, 'We are facing some trouble.. Try after some time ')
        form = ContactForm()

    contactData = ContactModal.objects.all()
    context = { 'contact' : 'active', 'fm' : ContactForm, 'contactData':contactData}
    return render(request, 'contact/contact.html', context)

def delete_contact(request, contact_id):
    contact = ContactModal.objects.get(id = contact_id)
    contact.delete()
    messages.success(request, 'Contact Successfully Deleted')
    return HttpResponseRedirect('/contact/', {'contact' : 'active'})