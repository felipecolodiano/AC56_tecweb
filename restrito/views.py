from django.shortcuts import render

def restrito(request, perfil):
    tipo = {
        "Aluno":{"nome":"Aluno"},
        "Professor":{"nome":"Professor"}
 
    }

    context = {
        "restrito": tipo[perfil]
    }
    return render(request, "restrito/perfil.html", context)
