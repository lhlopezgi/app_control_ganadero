# ganaderia/signals.py
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Finca, Vaca, Ternero  # Importa todos los modelos relevantes

@receiver(post_migrate)
def create_user_roles(sender, **kwargs):
    # Crear grupo Admin
    admin_group, created = Group.objects.get_or_create(name='Admin')
    if created:
        # Asignar todos los permisos al grupo Admin
        permissions = Permission.objects.all()
        admin_group.permissions.set(permissions)

    # Crear grupo Lectura
    lectura_group, created = Group.objects.get_or_create(name='Lectura')
    if created:
        # Asignar solo permisos de lectura para cada modelo
        for model in [Finca, Vaca, Ternero]:
            content_type = ContentType.objects.get_for_model(model)
            read_permissions = Permission.objects.filter(content_type=content_type, codename__startswith='view')
            lectura_group.permissions.add(*read_permissions)
