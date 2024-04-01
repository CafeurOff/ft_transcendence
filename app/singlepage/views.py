from django.shortcuts import render
from django.http import HttpResponse
from prometheus_client import Counter, Histogram, Gauge
from prometheus_client import generate_latest
from django.shortcuts import render, redirect
from .forms import UsernamesForm, PasswordForm, RememberForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import time

# View Index page : localhost:8000/
def index(request):
    message = ''
    if request.method == 'POST':
        form = UsernamesForm(request.POST)
        password_form = PasswordForm(request.POST)
        if form.is_valid() and password_form.is_valid():
            user = form.cleaned_data['usernames']
            password = password_form.cleaned_data['password'] 
            user = authenticate(username=user, password=password)
            if user:
                login(request, user)
                return redirect('/welcome/')
            else:
                message = 'Nom d’utilisateur ou mot de passe incorrect'
    else:
        form = UsernamesForm()
        password_form = PasswordForm()
    remember_form = RememberForm()
    return render(request, 'index.html', {'form': form, 'password_form': password_form, 'remember_form': remember_form, 'message': message})

def register(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if not form.is_valid():
            errors = form.errors.values()
            return render(request, 'register.html', {'form': form, 'errors': errors})
        else:
            user = form.save()
            return redirect('index')
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def welcome(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html', {'user': request.user})
    else:
        message = 'Vous devez être connecté pour accéder à cette page'
        return render(request, 'index.html', {'message': message, 'form': UsernamesForm(), 'password_form': PasswordForm()})

def gamepage(request):
    if request.user.is_authenticated:
        return render(request, 'gamepage.html', {'user': request.user})
    else:
        message = 'Vous devez être connecté pour accéder à cette page'
        return render(request, 'index.html', {'message': message, 'form': UsernamesForm(), 'password_form': PasswordForm()})

def game(request):
    return render(request, 'game.html')

def handler404(request):
    return render(request, '404.html', status=404)