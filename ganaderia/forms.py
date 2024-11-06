
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import ProduccionLeche, Finca, Vaca, Ternero, PesoVaca, PesoTernero


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

  
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
class ProduccionLecheForm(forms.ModelForm):
    class Meta:
        model = ProduccionLeche
        fields = ['vaca', 'cantidad_leche', 'observacion'] 
class FincaForm(forms.ModelForm):
    class Meta:
        model = Finca
        fields = ['nombre', 'hectareas', 'ciudad', 'asnm', 'temperatura', 'capacidad']
class VacaForm(forms.ModelForm):
    class Meta:
        model = Vaca
        fields = ['fecha_nacimiento', 'raza', 'color', 'observaciones']
class TerneroForm(forms.ModelForm):
    class Meta:
        model = Ternero
        fields = ['fecha_nacimiento', 'raza', 'color', 'sexo', 'observaciones']
    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data['fecha_nacimiento']

        # Aquí puedes agregar validaciones adicionales, si es necesario
        return fecha
class PesoVacaForm(forms.ModelForm):
    class Meta:
        model = PesoVaca
        fields = ['vaca', 'fecha', 'peso', 'observaciones']
        
    
class PesoTerneroForm(forms.ModelForm):
    class Meta:
        model = PesoTernero
        fields = ['ternero', 'fecha', 'peso', 'observaciones']
        







