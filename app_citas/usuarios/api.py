from typing import List
from ninja import NinjaAPI

from .chatbot import handle_thread, client
from .limiter import rate_limit

from .schemas import (
    UserSchema,
    MedicoSchema,
    PacienteSchema,
    EspecialidadSchema,
    HorarioSchema,
    CitaSchema,
    CreatePacienteSchema,
    CreateMedicoSchema,
    CreateEspecialidadSchema,
    MessageInput,
    ThreadResponse,
)
from .models import Medico, Paciente, Especialidad, Horarios, Cita


api = NinjaAPI()


@api.get("/test")
@rate_limit(requests_per_minute=1)
def test(request):
    return {"message": f"API funcionando!"}


# Endpoint para obtener información del usuario autenticado
@api.get("/me", response=UserSchema)
def me(request):
    user = request.user
    return {
        "username": user.username,
        "is_authenticated": user.is_authenticated,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }


# Endpoint para obtener la lista de médicos
@api.get("/medicos", response=list[MedicoSchema])
def get_medicos(request):
    return Medico.objects.select_related("user", "especialidad").all()


# Endpoint para obtener la lista de pacientes
@api.get("/pacientes", response=list[PacienteSchema])
def get_pacientes(request):
    return Paciente.objects.select_related("user", "medico_tratante").all()


# Endpoint para obtener la lista de citas
@api.get("/citas", response=list[CitaSchema])
def get_citas(request):
    return Cita.objects.select_related("paciente__user", "medico__user").all()


@api.post("/pacientes", response=PacienteSchema)
def create_paciente(request, data: CreatePacienteSchema):
    paciente = Paciente.objects.create(
        user_id=data.user_id,
        fecha_nacimiento=data.fecha_nacimiento,
        cedula=data.cedula,
        direccion=data.direccion,
        ocupacion=data.ocupacion,
        nombre_emergencia=data.nombre_emergencia,
        telefono_emergencia=data.telefono_emergencia,
        alergias=data.alergias,
        medicamento=data.medicamento,
    )
    return paciente


# Endpoint para crear un médico
@api.post("/medicos", response=MedicoSchema)
def create_medico(request, data: CreateMedicoSchema):
    medico = Medico.objects.create(
        user_id=data.user_id,
        especialidad_id=data.especialidad_id,
    )
    return medico


# Endpoint para crear una especialidad
@api.post("/especialidades", response=EspecialidadSchema)
def create_especialidad(request, data: CreateEspecialidadSchema):
    especialidad = Especialidad.objects.create(especialidad=data.especialidad)
    return especialidad


# Endpoint para manejar mensajes
@api.post("/chat", response=ThreadResponse)
def handle_thread_endpoint(request, payload: MessageInput):
    try:
        # Llama a la función handle_thread
        response, thread_id = handle_thread(
            client=client,
            message_content=payload.message_content,
            thread_id=payload.thread_id,
        )
        return {"response": response, "thread_id": thread_id}
    except Exception as e:
        return api.create_response(request, {"detail": str(e)}, status=500)
