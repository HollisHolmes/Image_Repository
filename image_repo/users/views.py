from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    # def __init__(self, *args, **kwargs):
    #     super(LoginForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs['placeholder'] = 'Username'
    #     self.fields['password'].widget.attrs['placeholder'] = 'Password'

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    # def __init__(self, *args, **kwargs):
    #     super(RegisterForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs['placeholder'] = 'Username'
    #     self.fields['password'].widget.attrs['placeholder'] = 'Password'
    #     self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
    #


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    else:
        return render(request, 'repo/index.html')

def login_view(request):
    # Prevent signed-in users from accessign the login view
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('repo:index'))
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
    return render(request, 'users/logout.html')

def register(request):
    # Prevent signed-in users from accessign the login view
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('repo:index'))
    if request.method == 'POST':
        # Get inputted username and password from form submission
        form = UserCreationForm(request.POST)
        print(form['username'], form['password1'])
        if form.is_valid():
            form.save()
            # If user is authenticated this will have returned a user

    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)