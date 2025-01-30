from django.shortcuts import render
from rest_framework import viewsets
from .models import Paciente, Medico
from .serializers import PacienteSerializer, MedicoSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
