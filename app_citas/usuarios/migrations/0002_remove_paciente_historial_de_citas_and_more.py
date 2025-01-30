# Generated by Django 5.1.3 on 2024-12-09 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='historial_de_citas',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='sintomas',
        ),
        migrations.AddField(
            model_name='paciente',
            name='cedula',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='paciente',
            name='direccion',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='medicamento',
            field=models.TextField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='paciente',
            name='medico_tratante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pacientes_tratados', to='usuarios.medico'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nombre_emergencia',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='paciente',
            name='ocupacion',
            field=models.TextField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='paciente',
            name='telefono_emergencia',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.especialidad'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='usuarios.usuario'),
        ),
    ]
