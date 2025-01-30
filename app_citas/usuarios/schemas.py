from ninja import Schema
from typing import Optional
from datetime import date


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class EspecialidadSchema(Schema):
    id: int
    especialidad: str


class MedicoSchema(Schema):
    id: int
    user: UserSchema
    especialidad: EspecialidadSchema


class PacienteSchema(Schema):
    id: int
    user: UserSchema
    fecha_nacimiento: Optional[date] = None
    cedula: Optional[str] = None
    direccion: Optional[str] = None
    ocupacion: Optional[str] = None
    nombre_emergencia: Optional[str] = None
    telefono_emergencia: Optional[str] = None
    alergias: Optional[str] = None
    medicamento: Optional[str] = None
    medico_tratante: Optional[MedicoSchema] = None

    @staticmethod
    def fecha_nacimiento_to_string(fecha: Optional[date]) -> Optional[str]:
        return fecha.strftime("%Y-%m-%d") if fecha else None

    def dict(self, **kwargs):
        data = super().dict(**kwargs)
        if isinstance(self.fecha_nacimiento, date):
            data["fecha_nacimiento"] = self.fecha_nacimiento_to_string(
                self.fecha_nacimiento
            )
        return data


class HorarioSchema(Schema):
    id: int
    medico: MedicoSchema
    tipo: str
    fecha_inicio: str
    fecha_fin: str


class CitaSchema(Schema):
    id: int
    paciente: PacienteSchema
    medico: MedicoSchema
    fecha_hora: str
    motivo: str
    sintomas: Optional[str] = None
    estado: str


class CreatePacienteSchema(Schema):
    user_id: int  # ID del usuario relacionado
    fecha_nacimiento: Optional[date] = None
    cedula: Optional[str] = None
    direccion: Optional[str] = None
    ocupacion: Optional[str] = None
    nombre_emergencia: Optional[str] = None
    telefono_emergencia: Optional[str] = None
    alergias: Optional[str] = None
    medicamento: Optional[str] = None


# Esquema para crear un médico
class CreateMedicoSchema(Schema):
    user_id: int  # ID del usuario relacionado
    especialidad_id: int  # ID de la especialidad


# Esquema para crear una especialidad
class CreateEspecialidadSchema(Schema):
    especialidad: str


# Esquema de entrada
class MessageInput(Schema):
    message_content: str
    thread_id: Optional[str] = None


# Esquema de salida
class ThreadResponse(Schema):
    response: str
    thread_id: str
