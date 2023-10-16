
from django.contrib import admin
from django.urls import path, include

from usuarios.views import index
from criancas_e_adolescentes.views import (
    registrar_crianca_e_adolescente, informacoes_registros
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index, name="index"), 

    path(
        "registrar-crianca-e-adolescente/",
        registrar_crianca_e_adolescente,
        name="registrar_crianca_e_adolescente",
    ),

    path(
        "criancas_e_adolescentes/<int:id>/",
        informacoes_registros,
        name="informacoes_registros",
    ),

]
