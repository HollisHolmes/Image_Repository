from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'repo/add.html')

def login(request):
    return render(request, 'repo/login.html')

def logout(request):
    return render(request, 'repo/logout.html')

def register(request):
    return render(request, 'repo/register.html')