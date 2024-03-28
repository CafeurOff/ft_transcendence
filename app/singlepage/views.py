from django.shortcuts import render
from django.http import HttpResponse
from prometheus_client import Counter, Histogram, Gauge
from prometheus_client import generate_latest
from django.shortcuts import render, redirect

# View Index page : localhost:8000/
def index(request):
    return render(request, 'index.html')

def game(request):
    return render(request, 'game.html')

def handler404(request, exception):
    return render(request, '404.html', status=404)


