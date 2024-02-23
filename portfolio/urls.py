"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from my_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
    path('project_details/<int:id>/', project_details, name='project_details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)