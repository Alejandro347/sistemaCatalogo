# Generated by Django 5.0.1 on 2024-01-11 16:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('disponibilidad', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=200)),
                ('transmision', models.CharField(max_length=50)),
                ('kilometraje', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.vehiculo')),
            ],
        ),
    ]
