from django.shortcuts import render

def curso(request, sigla):
    cursos = {
        "SI":{"nome":"Sistemas da Informação", "sigla":"SI", "disciplina":[{"nome":"Tecnologia Web", "sigla":"TW"},
        {"nome":"Engenharia de Software", "sigla":"ES"}]},

        "ADS":{"nome":"Análise e Desenvolvimento de Sistemas", "sigla":"ADS", "disciplina":[{"nome":"Libras", "sigla":"LBR"},
        {"nome":"Engenharia de Software", "sigla":"ES"}]},
        "BD":{"nome":"Banco de Dados","sigla":"BD","disciplina":[{"nome":"Gestão de Projetos", "sigla":"GP"},
        {"nome":"Linguagem de Programação II", "sigla":"LPII"}]},
        "GTI":{"nome":"Gestão de Tecnologia da Informação", "sigla":"GTI","disciplina":[{"nome":"Gestão de Projetos", "sigla":"GP"},
        {"nome":"Linguagem de Programação II", "sigla":"LPII"}]}
    }

    context = {
        "curso": cursos[sigla]
    }
    return render(request, "curriculo/curso.html", context)

def disciplina(request, sigla, abr):
    disciplinas = {
        "TW":{"nome":"Tecnologia Web", "sigla":"TW"},
        "ES":{"nome":"Engenharia de Software", "sigla":"ES"},
        "GP":{"nome":"Gestão de Projetos", "sigla":"GP"}, 
        "LBR":{"nome":"Libras", "sigla":"LBR"},
        "LPII":{"nome":"Linguagem de Programação II", "sigla":"LPII"},
    }

    context = {
        "disciplina": disciplinas[abr]
    }
    return render(request, "curriculo/disciplina.html", context)
