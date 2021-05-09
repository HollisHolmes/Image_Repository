from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'repo/add.html')

def main(request, name):
    context = {
        'name': name.capitalize()
    }
    return render(request, 'repo/index.html', context)

def login(request):
    return render(request, 'repo/login.html')