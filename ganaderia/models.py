from django.db import models


class Finca(models.Model):
    nombre = models.CharField(max_length=100)
    hectareas = models.DecimalField(max_digits=5, decimal_places=2)
    ubicacion = models.CharField(max_length=255)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    temperatura = models.DecimalField(max_digits=4, decimal_places=2)
    capacidad_animales = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Vaca(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_nacimiento = models.DateField()
    raza = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    observaciones = models.TextField(blank=True, null=True)
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name="vacas")
    
    def __str__(self):
        return f"Vaca {self.id} - {self.raza}"


class ProduccionLeche(models.Model):
    vaca = models.ForeignKey(Vaca, on_delete=models.CASCADE, related_name="producciones_leche")
    fecha = models.DateField()
    cantidad_leche = models.DecimalField(max_digits=5, decimal_places=2)
    observacion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Leche {self.fecha} - Vaca {self.vaca.id}"


class Peso(models.Model):
    vaca = models.ForeignKey(Vaca, on_delete=models.CASCADE, related_name="pesos")
    fecha = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"Peso {self.fecha} - Vaca {self.vaca.id}"


class Ternero(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_nacimiento = models.DateField()
    raza = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')])
    observaciones = models.TextField(blank=True, null=True)
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name="terneros")
    
    def __str__(self):
        return f"Ternero {self.id} - {self.raza}"


class PesoTernero(models.Model):
    ternero = models.ForeignKey(Ternero, on_delete=models.CASCADE, related_name="pesos")
    fecha = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    observaciones = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Peso {self.fecha} - Ternero {self.ternero.id}"





    
