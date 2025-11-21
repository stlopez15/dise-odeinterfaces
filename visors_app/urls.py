from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('subir/', views.subir_interface, name='subir_interface'),
    path('lista/', views.lista_interfaces, name='lista_interfaces'),
    path('ver/<int:id>/', views.ver_ra, name='ver_ra'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
