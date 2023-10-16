from django.contrib import messages
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from criancas_e_adolescentes.models import Crianca_e_Adolescente
from criancas_e_adolescentes.forms import Crianca_e_AdolescenteForm

def registrar_crianca_e_adolescente(request):

    form = Crianca_e_AdolescenteForm()

    if request.method == "POST":
        form = Crianca_e_AdolescenteForm(request.POST)
    
    if form.is_valid():
        crianca_e_adolescente = form.save(commit=False)

        crianca_e_adolescente.registrado_por = request.user.adm          
        crianca_e_adolescente.save()

        messages.success(
             request,
            "Registrado com sucesso"
        )

        return redirect("index")

    context = {
        "nome_pagina": "Registrar criança ou adolescente",
        "form": form,
    }
    
    return render(request, "registrar_crianca_e_adolescente.html", context)

def informacoes_registros(request, id):

    crianca_e_adolescente = get_object_or_404(
        Crianca_e_Adolescente, id=id
    )

    context = {
        "nome_pagina": "Informações da criança ou adolescente",
        "crianca_e_adolescente": Crianca_e_Adolescente,
    }
    
    return render(request, "informacoes_crianca_e_adolescente.html", context)