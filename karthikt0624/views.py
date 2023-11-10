


from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("HELLO Karthik")
# Create your views here.
# Create your views here.
def page2(request):
    return render(request, "contact/page2.html")

def createcontact(request):
    return render(request, "contact/createcontact.html")