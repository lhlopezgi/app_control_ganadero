
from django import views
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Finca, Vaca, ProduccionLeche, PesoVaca, Ternero, PesoTernero, Animal, Leche
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from .forms import (
    LoginForm,
    PesoTerneroForm, 
    ProduccionLecheForm, 
    FincaForm, 
    VacaForm, 
    TerneroForm, 
    PesoVacaForm
    )
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import path, reverse_lazy
from django.utils import timezone
from django.db.models import Sum, Count
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.views.decorators.http import require_POST



# Vista de inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido, {user.username}")
                return redirect('home')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'ganaderia/login.html', {'is_login_page': True})
# Vista de registro de usuarios
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Bienvenido, {user.username}. Tu cuenta ha sido creada.")
            return redirect('home')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = UserCreationForm()
    return render(request, 'ganaderia/register.html', {'form': form})
# Vista de cierre de sesión
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect('login')
# ganaderia/views.py
@login_required
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    # Para usuarios no autenticados, mostrar el formulario de inicio de sesión
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Información inválida.")
    else:
        form = AuthenticationForm()
    return render(request, 'ganaderia/home.html', {'form': form})
# Vista para registrar una nueva finca
@login_required
@permission_required('ganaderia.add_finca', raise_exception=True)
def finca_create(request):
    if request.method == 'POST':
        form = FincaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Finca registrada correctamente.")
            return redirect('dashboard')  # Asegúrate de que esta URL esté definida
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = FincaForm()
    return render(request, 'ganaderia/dashboard.html', {'form': form})



@login_required
@permission_required('ganaderia.add_vaca', raise_exception=True)
def vaca_create(request):
    if request.method == 'POST':
        form = VacaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vaca registrada correctamente.")
            return redirect('home')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = VacaForm()
    return render(request, 'ganaderia/dashboard.html', {'form': form})


# Vista para registrar un nuevo ternero
@login_required
@permission_required('ganaderia.add_ternero', raise_exception=True)
def ternero_create(request):
    if request.method == 'POST':
        form = TerneroForm(request.POST)
        print(f"Form data: {request.POST}")  # Imprime los datos recibidos del formulario

        if form.is_valid():
            form.save()
            messages.success(request, "Ternero registrado correctamente.")
            return redirect('home')
        else:
            print(f"Form errors: {form.errors}")  # Imprime los errores del formulario
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = TerneroForm()
    
    return render(request, 'ganaderia/dashboard.html', {'form': form})

@login_required
def dashboard(request):
    # Obtener la cantidad de animales en producción
    animales_en_produccion = Animal.objects.filter(en_produccion=True).count()
    # Obtener la cantidad de leche producida en los últimos 30 días
    leche_ultimos_30_dias = Leche.objects.filter(fecha__gte=datetime.now()-timedelta(days=30)).aggregate(Sum('cantidad'))['cantidad__sum'] or 0
    # Obtener la cantidad de leche producida hoy
    leche_hoy = Leche.objects.filter(fecha=datetime.now().date()).aggregate(Sum('cantidad'))['cantidad__sum'] or 0
    # Obtener la cantidad de terneros machos y hembras
    terneros_machos = Animal.objects.filter(genero='macho', en_crecimiento=True).count()
    terneros_hembras = Animal.objects.filter(genero='hembra', en_crecimiento=True).count()
    context = {
        'animales_en_produccion': animales_en_produccion,
        'leche_ultimos_30_dias': leche_ultimos_30_dias,
        'leche_hoy': leche_hoy,
        'terneros_machos': terneros_machos,
        'terneros_hembras': terneros_hembras,
    }
    return render(request, 'ganaderia/dashboard.html', context)
@login_required
@permission_required('ganaderia.add_produccionleche', raise_exception=True)
def produccion_leche_create(request):
    if request.method == 'POST':
        form = ProduccionLecheForm(request.POST)
        print(f"Form data: {request.POST}")  # Imprime los datos recibidos del formulario
        if form.is_valid():
            form.save()
            messages.success(request, "Producción de leche registrada correctamente.")
            return redirect('home')
        else:
            print(f"Form errors: {form.errors}")  # Imprime los errores del formulario
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = ProduccionLecheForm()
    return render(request, 'ganaderia/dashboard.html', {'form': form})


@login_required
@permission_required('ganaderia.add_pesovaca', raise_exception=True)
def peso_vaca_create(request):
    if request.method == "POST":
        form = PesoVacaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Peso de la vaca registrado correctamente.")
            return redirect('home')
        else:
            print("Errores del formulario:", form.errors)  # Depurar los errores
    else:
        form = PesoVacaForm()

    return render(request, 'ganaderia/dashboard.html', {'form': form})


@login_required
@permission_required('ganaderia.add_pesoternero', raise_exception=True)
def peso_ternero_create(request):
    if request.method == "POST":
        form = PesoTerneroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Peso del ternero registrado correctamente.")
            return redirect('home')  # O cualquier otra URL a la que desees redirigir después del éxito
        else:
            print("Errores del formulario:", form.errors)  # Depurar los errores
    else:
        form = PesoTerneroForm()

    return render(request, 'ganaderia/dashboard.html', {'form': form})


    
def leche_view(request):
    return render(request, 'ganaderia/leche.html')
def vacas(request):
    return render(request, 'ganaderia/vacas.html')
def terneros(request):
    return render(request, 'ganaderia/terneros.html')




















           


