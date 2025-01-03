from django.db import models
from usuarios.models import Medico, Paciente

ESTADO_CITA_CHOICES = [
    ("pendiente", "Pendiente"),
    ("confirmada", "Confirmada"),
    ("cancelada", "Cancelada"),
]

class Horario(models.Model):
    medico = models.ForeignKey(
        Medico, on_delete=models.CASCADE, related_name="horarios"
    )
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return f"Horario de {self.medico}: {self.fecha_inicio} - {self.fecha_fin}"

class Cita(models.Model):
    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, related_name="citas"
    )
    horario = models.ForeignKey(
        Horario, on_delete=models.CASCADE, related_name="citas", null=True, blank=True
    )
    motivo = models.TextField()
    sintomas = models.TextField(blank=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="citas")
    fecha_hora = models.DateTimeField()
    estado = models.CharField(
        max_length=50, choices=ESTADO_CITA_CHOICES, default="pendiente"
    )

    def __str__(self):
        return f"Cita de {self.paciente} con {self.medico} el {self.fecha_hora}"
