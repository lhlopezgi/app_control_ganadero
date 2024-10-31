
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Finca, Vaca, ProduccionLeche, Peso, Ternero, PesoTernero
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from .forms import LoginForm, ProduccionLecheForm, FincaForm, VacaForm, TerneroForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Sum, Count
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .forms import FincaForm, VacaForm, TerneroForm
from django.contrib.auth.decorators import login_required, permission_required




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
    
    return render(request, 'ganaderia/login.html', {'form': form})

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
    context = {
        'can_add_finca': request.user.has_perm('ganaderia.add_finca'),
        'can_add_vaca': request.user.has_perm('ganaderia.add_vaca'),
        'can_add_ternero': request.user.has_perm('ganaderia.add_ternero'),
    }
    return render(request, 'ganaderia/home.html', context)


# Vista para registrar una nueva finca
@login_required
@permission_required('ganaderia.add_finca', raise_exception=True)
def finca_create(request):
    if request.method == 'POST':
        form = FincaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Finca registrada correctamente.")
            return redirect('home')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = FincaForm()
    
    return render(request, 'ganaderia/finca_form.html', {'form': form})




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
    
    return render(request, 'ganaderia/vaca_form.html', {'form': form})

# Vista para registrar un nuevo ternero
@login_required
@permission_required('ganaderia.add_ternero', raise_exception=True)
def ternero_create(request):
    if request.method == 'POST':
        form = TerneroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ternero registrado correctamente.")
            return redirect('home')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = TerneroForm()
    
    return render(request, 'ganaderia/ternero_form.html', {'form': form})



@login_required
def dashboard(request):
    return render(request, 'ganaderia/dashboard.html')


