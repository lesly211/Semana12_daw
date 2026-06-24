from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/nuevo/', views.producto_nuevo, name='producto_nuevo'),
    path('contacto/', views.contacto, name='contacto'),
]
