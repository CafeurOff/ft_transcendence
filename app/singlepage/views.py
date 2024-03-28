from django.shortcuts import render
from django.http import HttpResponse
from prometheus_client import Counter, Histogram, Gauge
from prometheus_client import generate_latest
from django.shortcuts import render, redirect
from .forms import UsernamesForm, PasswordForm, RememberForm

# View Index page : localhost:8000/
def index(request):
    if request.method == 'POST':
        form = UsernamesForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['usernames']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember']
            user = authenticate(username=user, password=password)
            if user:
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)
                return redirect('game')
    else:
        form = UsernamesForm()
    password_form = PasswordForm()
    remember_form = RememberForm()
    return render(request, 'index.html', {'form': form, 'password_form': password_form, 'remember_form': remember_form}) 



def game(request):
    return render(request, 'game.html')

def handler404(request, exception):
    return render(request, '404.html', status=404)