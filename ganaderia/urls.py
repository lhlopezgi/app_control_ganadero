from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from ganaderia import views
from . import views



urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('', views.home, name='home'),
    path('finca/nueva/', views.finca_create, name='finca_create'),
    path('vaca/nueva/', views.vaca_create, name='vaca_create'),
    path('ternero/nueva/', views.ternero_create, name='ternero_create'),
    path('dashboard/', views.dashboard, name='dashboard'),
]




