from django.shortcuts import render
from django.http import HttpResponse
from prometheus_client import Counter, Histogram, Gauge
from prometheus_client import generate_latest
from django.shortcuts import render, redirect
from .forms import UsernamesForm, PasswordForm, RememberForm
from django.contrib.auth import login, authenticate, logout

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
            else:
                message = 'Nom d’utilisateur ou mot de passe incorrect'
    else:
        form = UsernamesForm()
        password_form = PasswordForm()
    remember_form = RememberForm()
    return render(request, 'index.html', {'form': form, 'password_form': password_form, 'remember_form': remember_form, 'message': message})

def register(request):
    message = ''
    if request.method == 'POST':
        form = UsernamesForm(request.POST)
        password_form = PasswordForm(request.POST)
        if form.is_valid() and password_form.is_valid():
            user = form.cleaned_data['usernames']
            password = password_form.cleaned_data['password']
            user = authenticate(username=user, password=password)
            if user:
                message = 'Nom d’utilisateur déjà utilisé'
            else:
                user = User.objects.create_user(username=user, password=password)
                user.save()
                user = authenticate(username=user, password=password)
                login(request, user)
                return redirect('index')
    else:
        form = UsernamesForm()
        password_form = PasswordForm()
    remember_form = RememberForm()
    return render(request, 'register.html', {'form': form, 'password_form': password_form, 'remember_form': remember_form, 'message': message})

def game(request):
    return render(request, 'game.html')

def handler404(request, exception):
    return render(request, '404.html', status=404)