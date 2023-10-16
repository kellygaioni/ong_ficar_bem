from django.shortcuts import render
from criancas_e_adolescentes.models import Crianca_e_Adolescente

def index(request): 

    todos_os_registros = Crianca_e_Adolescente.objects.all()

    nome_pagina = "Início da dashboard"

    context = {
        "nome_pagina": nome_pagina,
        "todos_os_registros": todos_os_registros,
    }
    
    return render(request, "index.html", context)