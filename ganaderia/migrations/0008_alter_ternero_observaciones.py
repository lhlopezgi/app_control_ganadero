# Generated by Django 5.1.2 on 2024-11-05 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganaderia', '0007_animal_leche'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ternero',
            name='observaciones',
            field=models.TextField(),
        ),
    ]