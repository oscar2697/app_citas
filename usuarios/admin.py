from django.contrib import admin
from .models import Especialidad, Medico, Paciente, Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Especialidad)
