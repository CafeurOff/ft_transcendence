from django.http import HttpResponse
from prometheus_client import Counter, Histogram, Gauge
from prometheus_client import generate_latest
from django.shortcuts import render, redirect

http_requests_total = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
http_request_duration_seconds = Histogram('http_request_duration_seconds', 'HTTP request duration', ['method', 'endpoint'])
active_users = Gauge('active_users', 'Number of active users')
http_errors_total = Counter('http_errors_total', 'Total HTTP errors', ['status_code', 'method', 'endpoint'])
http_response_size_bytes = Histogram('http_response_size_bytes', 'HTTP response size', ['method', 'endpoint'])
exception_counter = Counter('exceptions_raised_total', 'Total exceptions raised', ['exception_type'])

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

def metrics_view(request):
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)

def index(request):
    return render(request, 'index.html')

def my_view(request):
    http_requests_total.labels(request.method, request.path).inc()

texts = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tortor mauris, maximus semper volutpat vitae, varius placerat dui. Nunc consequat dictum est, at vestibulum est hendrerit at. Mauris suscipit neque ultrices nisl interdum accumsan. Sed euismod, ligula eget tristique semper, lecleo mi nec orci. Curabitur hendrerit, est in ",
        "Praesent euismod auctor quam, id congue tellus malesuada vitae. Ut sed lacinia quam. Sed vitae mattis metus, vel gravida ante. Praesent tincidunt nulla non sapien tincidunt, vitae semper diam faucibus. Nulla venenatis tincidunt efficitur. Integer justo nunc, egestas eget dignissim dignissim,  facilisis, dictum nunc ut, tincidunt diam.",
        "Morbi imperdiet nunc ac quam hendrerit faucibus. Morbi viverra justo est, ut bibendum lacus vehicula at. Fusce eget risus arcu. Quisque dictum porttitor nisl, eget condimentum leo mollis sed. Proin justo nisl, lacinia id erat in, suscipit ultrices nisi. Suspendisse placerat nulla at volutpat ultricies"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("No such section")
