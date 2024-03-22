from django.http import HttpResponse
from prometheus_client import Counter, Histogram, Gauge
from prometheus_client import generate_latest

http_requests_total = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
http_request_duration_seconds = Histogram('http_request_duration_seconds', 'HTTP request duration', ['method', 'endpoint'])
active_users = Gauge('active_users', 'Number of active users')
http_errors_total = Counter('http_errors_total', 'Total HTTP errors', ['status_code', 'method', 'endpoint'])
http_response_size_bytes = Histogram('http_response_size_bytes', 'HTTP response size', ['method', 'endpoint'])

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

def metrics_view(request):
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)

def index(request):
    return HttpResponse("Welcome to my Django application!")

def my_view(request):
    # Votre logique de vue ici
    http_requests_total.labels(request.method, request.path).inc()
    # Autres opérations de vue
