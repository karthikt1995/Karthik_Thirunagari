

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def index(request):
    return HttpResponse("HELLO Karthik")
#Create your views here.
#Create your views here.
#main page or start page
def startpage(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/startpage.html', {'contacts': contacts})
#contact details 
def contact_detail(request, serial_number):
    contact = get_object_or_404(Contact, serial_number=serial_number)
    return render(request, 'contact/contact_detail.html', {'contact': contact})
#create contact page
def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('startpage')
    else:
        form = ContactForm()

    return render(request, 'contact/create_contact.html', {'form': form})

#update contact

def update_contact(request, serial_number):
    contact = get_object_or_404(Contact, serial_number=serial_number)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('startpage')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contact/update_contact.html', {'form': form, 'contact': contact})
#deletecontact
def delete_contact(request, serial_number):
    contact = get_object_or_404(Contact, serial_number=serial_number)

    if request.method == 'POST':
        contact.delete()
        return redirect('startpage')

    return render(request, 'contact/delete_contact.html', {'contact': contact})