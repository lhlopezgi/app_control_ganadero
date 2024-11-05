from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from ganaderia import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('finca/nueva/', views.finca_create, name='finca_create'),
    path('vaca/nueva/', views.vaca_create, name='vaca_create'),
    path('ternero/crear/', views.ternero_create, name='ternero_create'),
    path('pesovaca/nueva/', views.peso_vaca_create, name='peso_vaca_create'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('produccionleche/nueva/', views.produccion_leche_create, name='produccion_leche_create'),
    path('pesoternero/nueva/', views.peso_ternero_create, name='peso_ternero_create'),
    path('leche/', views.leche_view, name='leche'),
    path('vacas/', views.vacas, name='vacas'),
    path('terneros/', views.terneros, name='terneros'),   
]





