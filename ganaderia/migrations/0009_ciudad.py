# Generated by Django 5.1.2 on 2024-11-07 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganaderia', '0008_alter_ternero_observaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
