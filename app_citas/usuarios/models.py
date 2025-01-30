from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    rol = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rol})"


class Especialidad(models.Model):
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.especialidad


class Medico(models.Model):
    user = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name="medico"
    )
    nombre_medico = models.CharField(max_length=100, default='Nombre')
    apellido_medico = models.CharField(max_length=100, default='Apellido')
    especialidad = models.CharField(max_length=100, default='General')  # Provide a default value
    horario_disponible = models.DateTimeField()
    horario_no_disponible = models.DateTimeField()

    def __str__(self):
        return f"Dr. {self.nombre_medico} {self.apellido_medico} - {self.especialidad}"

class Paciente(models.Model):
    user = models.OneToOneField(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name="paciente"
    )
    email = models.EmailField(max_length=100, default='Email')
    telefono = models.CharField(max_length=10, default='Phone')
    nombre = models.CharField(max_length=100, default='Name')
    consentimientoPrivacidad = models.BooleanField(default=False)
    genero = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    ocupacion = models.CharField(max_length=100, null=True, blank=True)
    numero_emergencia = models.CharField(max_length=20, null=True, blank=True)
    proveedor_seguro = models.CharField(max_length=100, null=True, blank=True)
    alergias = models.TextField(null=True, blank=True)
    medicacion = models.TextField(null=True, blank=True)
    historial_medico_familiar = models.TextField(null=True, blank=True)
    historial_pasado_medico = models.TextField(null=True, blank=True)
    tipo_identificacion = models.CharField(max_length=100, null=True, blank=True)
    numero_cedula = models.CharField(max_length=100, null=True, blank=True)
    identificationDocumentId = models.CharField(max_length=100, null=True, blank=True)
    numero_de_seguro = models.CharField(max_length=100, null=True, blank=True)
    identificationDocumentUrl = models.URLField(null=True, blank=True)
    medico_tratante = models.ForeignKey(
        Medico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pacientes_tratados'
    )
    consentimiento_tratamiento = models.BooleanField(null=True, blank=True)
    disclosureConsent = models.BooleanField(null=True, blank=True)
    nombre_emergencia = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


