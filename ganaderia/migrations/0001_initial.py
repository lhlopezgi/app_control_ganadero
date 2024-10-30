

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('hectareas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ubicacion', models.CharField(max_length=255)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temperatura', models.DecimalField(decimal_places=2, max_digits=4)),
                ('capacidad_animales', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ternero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_nacimiento', models.DateField()),
                ('raza', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], max_length=10)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terneros', to='ganaderia.finca')),
            ],
        ),
        migrations.CreateModel(
            name='PesoTernero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('ternero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pesos', to='ganaderia.ternero')),
            ],
        ),
        migrations.CreateModel(
            name='Vaca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_nacimiento', models.DateField()),
                ('raza', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacas', to='ganaderia.finca')),
            ],
        ),
        migrations.CreateModel(
            name='ProduccionLeche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cantidad_leche', models.DecimalField(decimal_places=2, max_digits=5)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('vaca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producciones_leche', to='ganaderia.vaca')),
            ],
        ),
        migrations.CreateModel(
            name='Peso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vaca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pesos', to='ganaderia.vaca')),
            ],
        ),
    ]
