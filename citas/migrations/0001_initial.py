# Generated by Django 5.1.3 on 2024-12-03 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cita",
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
                ("fecha_hora", models.DateTimeField()),
                ("estado", models.CharField(max_length=50)),
                ("motivo", models.TextField()),
                (
                    "medico",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="citas",
                        to="usuarios.medico",
                    ),
                ),
                (
                    "paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="citas",
                        to="usuarios.paciente",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Horario",
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
                ("fecha_inicio", models.DateTimeField()),
                ("fecha_fin", models.DateTimeField()),
                (
                    "medico",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="horarios",
                        to="usuarios.medico",
                    ),
                ),
            ],
        ),
    ]
