from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, dashboard, registro_usuario
from .views import agregar_produccion_leche

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('registro/', registro_usuario, name='registro'),
    path('agregar-produccion-leche/', agregar_produccion_leche, name='agregar_produccion_leche'),
]
