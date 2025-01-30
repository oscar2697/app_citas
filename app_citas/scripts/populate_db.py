# python manage.py shell

from usuarios.models import Usuario, Medico, Paciente, Especialidad
from citas.models import Cita, Horario

# Crear especialidades
especialidad_cardiologia = Especialidad.objects.create(especialidad="Cardiología")
especialidad_ortopedia = Especialidad.objects.create(especialidad="Ortopedia")

# Crear médicos
usuario_medico1 = Usuario.objects.create(
    nombre="Dr. Juan",
    apellido="Hernández",
    correo="juan.hernandez@example.com",
    telefono="123456789",
    rol="medico",
    contraseña="medico123",
)
medico1 = Medico.objects.create(
    user=usuario_medico1, especialidad=especialidad_cardiologia
)

usuario_medico2 = Usuario.objects.create(
    nombre="Dra. María",
    apellido="Gómez",
    correo="maria.gomez@example.com",
    telefono="987654321",
    rol="medico",
    contraseña="medico456",
)
medico2 = Medico.objects.create(
    user=usuario_medico2, especialidad=especialidad_ortopedia
)

# Crear horarios para médicos
Horario.objects.create(
    medico=medico1, fecha_inicio="2024-12-04 09:00:00", fecha_fin="2024-12-04 12:00:00"
)
Horario.objects.create(
    medico=medico2, fecha_inicio="2024-12-04 13:00:00", fecha_fin="2024-12-04 17:00:00"
)

# Crear pacientes
usuario_paciente1 = Usuario.objects.create(
    nombre="Carlos",
    apellido="López",
    correo="carlos.lopez@example.com",
    telefono="123123123",
    rol="paciente",
    contraseña="paciente123",
)
paciente1 = Paciente.objects.create(
    user=usuario_paciente1, sintomas="Dolor de pecho", alergias="Aspirina"
)

usuario_paciente2 = Usuario.objects.create(
    nombre="Ana",
    apellido="Martínez",
    correo="ana.martinez@example.com",
    telefono="321321321",
    rol="paciente",
    contraseña="paciente456",
)
paciente2 = Paciente.objects.create(
    user=usuario_paciente2, sintomas="Dolor de espalda", alergias="Ninguna"
)

usuario_paciente3 = Usuario.objects.create(
    nombre="Pedro",
    apellido="González",
    correo="pedro.gonzalez@example.com",
    telefono="456456456",
    rol="paciente",
    contraseña="paciente789",
)
paciente3 = Paciente.objects.create(
    user=usuario_paciente3, sintomas="Dolor de rodilla", alergias="Penicilina"
)

# Crear citas
Cita.objects.create(
    paciente=paciente1,
    medico=medico1,
    fecha_hora="2024-12-05 10:00:00",
    estado="pendiente",
    motivo="Revisión cardiológica",
)
Cita.objects.create(
    paciente=paciente2,
    medico=medico2,
    fecha_hora="2024-12-05 14:00:00",
    estado="confirmada",
    motivo="Evaluación de dolor de espalda",
)
Cita.objects.create(
    paciente=paciente3,
    medico=medico2,
    fecha_hora="2024-12-05 15:30:00",
    estado="pendiente",
    motivo="Consulta de ortopedia",
)
Cita.objects.create(
    paciente=paciente1,
    medico=medico1,
    fecha_hora="2024-12-06 09:00:00",
    estado="confirmada",
    motivo="Seguimiento de tratamiento",
)

print("Datos creados: 2 médicos, 3 pacientes, 4 citas y sus horarios asociados.")
