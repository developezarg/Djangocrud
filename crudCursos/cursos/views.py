from django.shortcuts import render
from django.shortcuts import redirect
from .models import Curso

def inicio(request):
    listacursos=Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos":listacursos})


def registroCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    nota = request.POST['numNotas']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, nota=nota)
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    nota = request.POST['numNotas']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.nota = nota
    curso.save()

    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    return redirect('/')