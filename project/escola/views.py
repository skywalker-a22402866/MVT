from django.shortcuts import render
from .models import Curso, Professor, Aluno

# Create your views here.
def cursos_view(request):
    cursos=Curso.objects.all()       
    return render(request, 'escola/cursos.html', {'cursos': cursos})

def professores_view(request):
    professores = Professor.objects.all()
    return render(request, 'escola/professores.html', {'professores': professores})


def alunos_view(request):
    alunos = Aluno.objects.all()
    return render(request, 'escola/alunos.html', {'alunos': alunos})

def curso_view(request, id):
    curso=Curso.objects.get(id=id)       
    return render(request, 'escola/curso.html', {'curso': curso})