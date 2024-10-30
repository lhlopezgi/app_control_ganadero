
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Finca, Vaca, ProduccionLeche, Peso, Ternero, PesoTernero
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from .forms import LoginForm, ProduccionLecheForm  
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Sum, Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def crear_grupos():
   
    admin, created = Group.objects.get_or_create(name="Admin")
    lectura, created = Group.objects.get_or_create(name="Lectura")

  
    content_types = ContentType.objects.get_for_models(Finca, Vaca, ProduccionLeche, Peso, Ternero, PesoTernero)
    permisos = Permission.objects.filter(content_type__in=content_types.values())

    admin.permissions.set(permisos)
    lectura.permissions.set(permisos.filter(codename__startswith="view_"))

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')  
        else:
           
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = UserCreationForm()
    return render(request, 'ganaderia/registro.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'ganaderia/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

class FincaListView(ListView):
    model = Finca
    template_name = 'ganaderia/finca_list.html'
    context_object_name = 'fincas'

class FincaCreateView(CreateView):
    model = Finca
    template_name = 'ganaderia/finca_form.html'
    fields = '__all__'  
    success_url = reverse_lazy('finca_list')

class FincaUpdateView(UpdateView):
    model = Finca
    template_name = 'ganaderia/finca_form.html'
    fields = '__all__'
    success_url = reverse_lazy('finca_list')

class FincaDeleteView(DeleteView):
    model = Finca
    template_name = 'ganaderia/finca_confirm_delete.html'
    success_url = reverse_lazy('finca_list')

class VacaListView(ListView):
    model = Vaca
    template_name = 'ganaderia/vaca_list.html'
    context_object_name = 'vacas'

class VacaCreateView(CreateView):
    model = Vaca
    template_name = 'ganaderia/vaca_form.html'
    fields = '__all__'
    success_url = reverse_lazy('vaca_list')

class VacaUpdateView(UpdateView):
    model = Vaca
    template_name = 'ganaderia/vaca_form.html'
    fields = '__all__'
    success_url = reverse_lazy('vaca_list')

class VacaDeleteView(DeleteView):
    model = Vaca
    template_name = 'ganaderia/vaca_confirm_delete.html'
    success_url = reverse_lazy('vaca_list')

class ProduccionLecheListView(ListView):
    model = ProduccionLeche
    template_name = 'ganaderia/produccion_leche_list.html'
    context_object_name = 'producciones'

class ProduccionLecheCreateView(CreateView):
    model = ProduccionLeche
    template_name = 'ganaderia/produccion_leche_form.html'
    fields = '__all__'
    success_url = reverse_lazy('produccion_leche_list')

class ProduccionLecheUpdateView(UpdateView):
    model = ProduccionLeche
    template_name = 'ganaderia/produccion_leche_form.html'
    fields = '__all__'
    success_url = reverse_lazy('produccion_leche_list')

class ProduccionLecheDeleteView(DeleteView):
    model = ProduccionLeche
    template_name = 'ganaderia/produccion_leche_confirm_delete.html'
    success_url = reverse_lazy('produccion_leche_list')

class PesoListView(ListView):
    model = Peso
    template_name = 'ganaderia/peso_list.html'
    context_object_name = 'pesos'

class PesoCreateView(CreateView):
    model = Peso
    template_name = 'ganaderia/peso_form.html'
    fields = '__all__'
    success_url = reverse_lazy('peso_list')

class PesoUpdateView(UpdateView):
    model = Peso
    template_name = 'ganaderia/peso_form.html'
    fields = '__all__'
    success_url = reverse_lazy('peso_list')

class PesoDeleteView(DeleteView):
    model = Peso
    template_name = 'ganaderia/peso_confirm_delete.html'
    success_url = reverse_lazy('peso_list')

class TerneroListView(ListView):
    model = Ternero
    template_name = 'ganaderia/ternero_list.html'
    context_object_name = 'terneros'

class TerneroCreateView(CreateView):
    model = Ternero
    template_name = 'ganaderia/ternero_form.html'
    fields = '__all__'
    success_url = reverse_lazy('ternero_list')

class TerneroUpdateView(UpdateView):
    model = Ternero
    template_name = 'ganaderia/ternero_form.html'
    fields = '__all__'
    success_url = reverse_lazy('ternero_list')

class TerneroDeleteView(DeleteView):
    model = Ternero
    template_name = 'ganaderia/ternero_confirm_delete.html'
    success_url = reverse_lazy('ternero_list')

class PesoTerneroListView(ListView):
    model = PesoTernero
    template_name = 'ganaderia/peso_ternero_list.html'
    context_object_name = 'pesos'

class PesoTerneroCreateView(CreateView):
    model = PesoTernero
    template_name = 'ganaderia/peso_ternero_form.html'
    fields = '__all__'
    success_url = reverse_lazy('peso_ternero_list')

def dashboard(request):
    
    total_vacas = Vaca.objects.count()

    
    fecha_hace_30_dias = timezone.now() - timezone.timedelta(days=30)
    leche_ultimos_30_dias = ProduccionLeche.objects.filter(fecha__gte=fecha_hace_30_dias).aggregate(Sum('cantidad_leche'))['cantidad_leche__sum'] or 0

   
    fecha_hoy = timezone.now().date()
    leche_hoy = ProduccionLeche.objects.filter(fecha=fecha_hoy).aggregate(Sum('cantidad_leche'))['cantidad_leche__sum'] or 0

   
    total_terneros = Ternero.objects.values('sexo').annotate(cantidad=Count('id'))

    cantidad_machos = next((item['cantidad'] for item in total_terneros if item['sexo'] == 'Macho'), 0)
    cantidad_hembras = next((item['cantidad'] for item in total_terneros if item['sexo'] == 'Hembra'), 0)

    context = {
        'total_vacas': total_vacas,
        'leche_ultimos_30_dias': leche_ultimos_30_dias,
        'leche_hoy': leche_hoy,
        'cantidad_machos': cantidad_machos,
        'cantidad_hembras': cantidad_hembras,
    }
    
    return render(request, 'ganaderia/dashboard.html', context)

def agregar_produccion_leche(request):
    if request.method == 'POST':
        form = ProduccionLecheForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Información diaria registrada exitosamente.')
            return redirect('dashboard')  
        else:
            
            messages.error(request, 'Error al registrar la producción de leche. Corrige los errores.')
    else:
        form = ProduccionLecheForm()
    
    return render(request, 'ganaderia/agregar_produccion_leche.html', {'form': form})








