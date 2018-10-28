from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContatoForm

# Create your views here.
def home(request):
    context = {
        "titulo": "Outro Título"

    }
    return render(request, "index.html", context)
    
def contato(request):
    context = { }

    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.enviar_email()
            context["mensagem"] = "Mensagem enviada com sucesso!"
        
        else:
            context["mensagem"] = "Problemas ao enviar a mensagem"
    else:
        form = ContatoForm()
        context["form"] = form
        context["mensagem"] = "Foi um GET"

    return render(request, "contato.html", context)

def curso(request):
    context = {
        "titulo": "Curso"
    }
    return render(request, "curso.html", context)


def entrar(request):
    context = {
        "titulo": "Login"
    }
    return render(request, "entrar.html", context)
