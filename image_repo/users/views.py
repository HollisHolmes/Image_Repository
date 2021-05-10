from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='')
    password = forms.CharField(widget=forms.PasswordInput(), label='')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    else:
        return render(request, 'repo/index.html')

def login_view(request):
    if request.method == 'POST':
        # Get inputted username and password from form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # If user is authenticated this will have returned a user
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            context = {
                'message': 'Invalid Credentials',
                'form': LoginForm()
            }
            return render(request, 'users/login.html', context)
    context = {'form': LoginForm()}
    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    context = {'message': 'Logged Out'}
    return render(request, 'users/login.html', context)

def register(request):
    return render(request, 'users/register.html')