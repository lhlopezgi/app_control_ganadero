from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Finca(models.Model):
    nombre = models.CharField(max_length=100)
    hectareas = models.DecimalField(max_digits=6, decimal_places=2)
    ciudad = models.CharField(max_length=100)
    asnm = models.IntegerField(default=0)
    temperatura = models.DecimalField(max_digits=4, decimal_places=1)
    capacidad = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre
class Vaca(models.Model):
    fecha_nacimiento = models.DateField()
    raza = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    observaciones = models.TextField(blank=True, null=True)
    es_productiva = models.BooleanField(default=True)  # Para saber si está en producción
    def __str__(self):
        return f"{self.raza} ({self.id})"
class Ternero(models.Model):
    SEXO_CHOICES = [
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    ]
    fecha_nacimiento = models.DateField()
    raza = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    sexo = models.CharField(max_length=6, choices=SEXO_CHOICES)
    observaciones = models.TextField()
    def __str__(self):
        return f"{self.raza} ({self.sexo})"
class ProduccionLeche(models.Model):
    vaca = models.ForeignKey(Vaca, on_delete=models.CASCADE, related_name="producciones_leche")
    fecha = models.DateField(auto_now_add=True)  # Se puede establecer automáticamente la fecha
    cantidad_leche = models.DecimalField(max_digits=5, decimal_places=2)
    observacion = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Leche producida: {self.cantidad} litros"
class PesoTernero(models.Model):
    ternero = models.ForeignKey(Ternero, on_delete=models.CASCADE)
    fecha = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)  # Puedes ajustar los dígitos según lo necesites
    observaciones = models.TextField(blank=True, null=True)  # Campo opcional para observaciones
    def __str__(self):
        return f"{self.ternero} - {self.peso} kg en {self.fecha}"
class PesoVaca(models.Model):
    vaca = models.ForeignKey(Vaca, on_delete=models.CASCADE)
    fecha = models.DateField()  # Asegúrate de tener este campo
    peso = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo de un campo de peso
    observaciones = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.vaca} - {self.peso} kg en {self.fecha}"
class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    en_produccion = models.BooleanField(default=False)
    genero = models.CharField(max_length=6, choices=[('macho', 'Macho'), ('hembra', 'Hembra')])
    en_crecimiento = models.BooleanField(default=False)
    vaca = models.ForeignKey(Vaca, on_delete=models.CASCADE, related_name='animales', default=2)  # Aquí usas el ID de la vaca

class Leche(models.Model):
    cantidad = models.FloatField()
    fecha = models.DateField(auto_now_add=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)










    
