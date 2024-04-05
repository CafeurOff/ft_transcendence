from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UsernamesForm, PasswordForm, SignupForm, UpdateUserNameForm, UpdatePictureForm, UpdatePasswordForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from singlepage.models import User
import time

# View Index page : localhost:8000/
def index(request):
    if request.user.is_authenticated:
        return redirect('/welcome/')
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
    return render(request, 'index.html', {'form': form, 'password_form': password_form, 'message': message})

# View Register page : localhost:8000/register/
def register(request):
    if request.user.is_authenticated:
        return redirect('/welcome/')
    form = SignupForm()
    message = ''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            login(request, user)
            return render(request, 'welcome.html')
        else:
            message = 'Votre formulaire contient des erreurs'
            return render(request, 'register.html', {'form': form, 'message': message})
    return render(request, 'register.html', {'form': form})


@login_required
def settings(request):
    picture_form = UpdatePictureForm(instance=request.user)
    form = UpdateUserNameForm(instance=request.user)
    password_form = UpdatePasswordForm(instance=request.user)
    if request.method == 'POST':
        picture_form = UpdatePictureForm(request.POST, request.FILES, instance=request.user)
        form = UpdateUserNameForm(request.POST, instance=request.user)
        password_form = UpdatePasswordForm(request.POST, instance=request.user)
        if form.is_valid() and picture_form.is_valid() and password_form.is_valid():
            user = form.save()
            picture_form.save()
            new_password = password_form.cleaned_data['password']
            if new_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
        else:
            picture_form = UpdatePictureForm(instance=request.user)
            form = UpdateUserNameForm(instance=request.user)
    return render(request, 'settings.html', {'form': form, 'picture_form': picture_form, 'password_form': password_form,})

@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

@login_required
def welcome(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html', {'user': request.user})
    else:
        message = 'Vous devez être connecté pour accéder à cette page'
        return render(request, 'index.html', {'message': message, 'form': UsernamesForm(), 'password_form': PasswordForm()})

@login_required
def gamepage(request):
    if request.user.is_authenticated:
        return render(request, 'gamepage.html', {'user': request.user})
    else:
        message = 'Vous devez être connecté pour accéder à cette page'
        return render(request, 'index.html', {'message': message, 'form': UsernamesForm(), 'password_form': PasswordForm()})
 
@login_required
def game(request):
    if request.method == 'POST':
        request.user.total_matches += 1
        request.user.save()
        return JsonResponse({'success': True})
    return render(request, 'game.html')

@login_required
def gameia(request):
    if request.method == 'POST':
        request.user.total_matches += 1
        request.user.save()
        return JsonResponse({'success': True})
    return render(request, 'ia.html')

@login_required
def update_score(request):
    if request.method == 'POST':
        # Augmenter le score du joueur 1
        user = request.user
        user.win += 1
        user.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
@login_required
def update_loss(request):
    if request.method == 'POST':
        # Augmenter le score du joueur 1
        user = request.user
        user.lose += 1
        user.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


def handler404(request, exception):
    return render(request, 'base/404.html', status=404)
    
def handler500(request):
    return render(request, 'base/500.html', status=500)