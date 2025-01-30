# Generated by Django 5.1.3 on 2024-12-03 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Especialidad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("especialidad", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("correo", models.EmailField(max_length=254, unique=True)),
                ("telefono", models.CharField(blank=True, max_length=15, null=True)),
                ("rol", models.CharField(max_length=50)),
                ("contraseña", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Paciente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sintomas", models.TextField()),
                ("alergias", models.TextField(blank=True, null=True)),
                ("historial_de_citas", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="paciente",
                        to="usuarios.usuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Medico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("horarios_disponibles", models.TextField()),
                (
                    "especialidad",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="usuarios.especialidad",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medico",
                        to="usuarios.usuario",
                    ),
                ),
            ],
        ),
    ]
