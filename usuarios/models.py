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


class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='paciente')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    userId = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    privacyConsent = models.BooleanField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    emergencyContactNumber = models.CharField(max_length=20, null=True, blank=True)
    insuranceProvider = models.CharField(max_length=255, null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    currentMedication = models.TextField(null=True, blank=True)
    familyMedicalHistory = models.TextField(null=True, blank=True)
    pastMedicalHistory = models.TextField(null=True, blank=True)
    identificationType = models.CharField(max_length=255, null=True, blank=True)
    identificationNumber = models.CharField(max_length=255, null=True, blank=True)
    identificationDocumentId = models.CharField(max_length=255, null=True, blank=True)
    insurancePolicyNumber = models.CharField(max_length=255, null=True, blank=True)
    identificationDocumentUrl = models.URLField(null=True, blank=True)
    primaryPhysician = models.CharField(max_length=255, null=True, blank=True)
    treatmentConsent = models.BooleanField(null=True, blank=True)
    disclosureConsent = models.BooleanField(null=True, blank=True)
    emergencyContactName = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='medico')
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    horario_disponible = models.CharField(max_length=255)
    horario_no_disponible = models.CharField(max_length=255)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} - {self.especialidad}"
