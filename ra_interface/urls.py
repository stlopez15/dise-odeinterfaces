"""
URL configuration for ra_interface project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from visors_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("subir/", views.subir_interface, name="subir_interface"),
    path("lista/", views.lista_interfaces, name="lista_interfaces"),
    path("ver/<int:id>/", views.ver_ra, name="ver_ra"),
]

# 👉 Servir MEDIA
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 👉 Servir STATIC (muy importante para /static/patterns/hiro.patt)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


