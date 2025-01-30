from django.shortcuts import render
from rest_framework import viewsets
from .models import Paciente, Medico, Cita, Horario
from .serializers import PacienteSerializer, MedicoSerializer, CitaSerializer, HorarioSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Cita.objects.all()
        return Cita.objects.filter(medico__user=user)
