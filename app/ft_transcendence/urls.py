"""
URL configuration for ft_transcendence project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from singlepage import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler500

handler500 = 'singlepage.views.handler500'
handler404 = 'singlepage.views.handler404'

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django_prometheus.urls')), # Is the localhost:8000/metrics endpoint
    path('admin/', admin.site.urls),
    path('game/', views.game, name='game'),
    path('game/ia', views.gameia, name='gameia'),
    path('update_score/', views.update_score, name='update_score'),
    path('update_loss/', views.update_loss, name='update_loss'),
    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('gamepage/', views.gamepage, name='gamepage'),
    path('settings/', views.settings, name='settings'),
    path('404/', views.handler404, name='404')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)