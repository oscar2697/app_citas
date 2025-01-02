from django.db import models

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
        Usuario, on_delete=models.CASCADE, related_name="medico"
    )
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, null=True)
    horarios_disponibles = models.TextField()

    def __str__(self):
        return f"Médico: {self.user.nombre} {self.user.apellido} - {self.especialidad}"


class Paciente(models.Model):
    user = models.OneToOneField(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name="paciente"
    )
    fecha_nacimiento = models.DateField(null=True, blank=True)
    cedula = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(max_length=100, blank=True)
    ocupacion = models.TextField(max_length=20, blank=True)
    nombre_emergencia = models.TextField(max_length=100, blank=True)
    telefono_emergencia = models.CharField(max_length=10, blank=True)
    alergias = models.TextField(null=True, blank=True)
    medicamento = models.TextField(max_length=20, blank=True)
    medico_tratante = models.ForeignKey(
        Medico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pacientes_tratados'
    )

    def __str__(self):
        return f"Paciente: {self.user.nombre} {self.user.apellido}"
