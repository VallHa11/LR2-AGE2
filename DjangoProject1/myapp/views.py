from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def doors(request):
    return render(request, 'myapp/doors.html')