

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def index(request):
    return HttpResponse("HELLO Karthik")
#Create your views here.
#Create your views here.

def startpage(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/startpage.html', {'contacts': contacts})