from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from datetime import date

from .forms.curso_form import CursoForm


def home(request):
    num_cursos = Curso.objects.filter(estado="publicado").count()
    num_estudiantes = Inscripcion.objects.values("estudiante").count()

    proximo_curso = (
        Curso.objects.filter(estado="publicado", fecha_publicacion__gt=date.today())
        .order_by("fecha_publicacion")
        .first()
    )

    cursos_destacados = Curso.objects.filter(estado="publicado", destacado=True)[:3]

    cursos_destacados_data = []
    # Recorro el iterable (Queryset) cursos_destacados
    # y por cada curso, creo un diccionario con los datos
    for curso in cursos_destacados:
        curso_data = {
            "id": curso.id,
            "nombre": curso.nombre,
            "descripcion": curso.descripcion,
            "imagen": curso.imagen.url,
        }
        cursos_destacados_data.append(curso_data)

    context = {
        "num_cursos": num_cursos,
        "num_estudiantes": num_estudiantes,
        "proximo_curso": proximo_curso,
        "cursos_destacados": cursos_destacados_data,
    }

    return render(request, "cursos/home.html", context)


def curso_list(request):
    cursos = Curso.objects.select_related("categoria").filter(estado="publicado")
    cursos_data = []
    for curso in cursos:
        curso_data = {
            "id": curso.id,
            "nombre": curso.nombre,
            "descripcion": curso.descripcion,
            "precio": curso.precio,
            "fecha_publicacion": curso.fecha_publicacion,
            "categoria": curso.categoria.nombre,
            "duracion": curso.duracion,
            "num_estudiantes": curso.estudiantes.count(),
            "imagen": curso.imagen.url,
        }
        cursos_data.append(curso_data)

    context = {"cursos": cursos_data}
    return render(request, "cursos/curso_list.html", context=context)


def curso_detail(request, curso_id):
    curso = (
        Curso.objects.prefetch_related("estudiantes")
        .prefetch_related("instructor")
        .get(id=curso_id)
    )

    curso_data = {
        "id": curso.id,
        "nombre": curso.nombre,
        "descripcion": curso.descripcion,
        "precio": curso.precio,
        "fecha_publicacion": curso.fecha_publicacion,
        "categoria": curso.categoria.nombre,
        "duracion": curso.duracion,
        "num_estudiantes": curso.estudiantes.count(),
        "imagen": curso.imagen.url,
        "instructor": curso.instructor,
        "estado": curso.estado,
        "imagen_instructor": curso.instructor.avatar.url,
        "contenido": curso.contenido,
    }
    context = {"curso": curso_data}
    return render(request, "cursos/curso_detail.html", context=context)


def create_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("curso_list")
    else:  # Método GET
        form = CursoForm()

    context = {"titulo": "Nuevo Curso", "form": form, "submit": "Crear Curso"}
    return render(request, "cursos/curso_form.html", context)


def update_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == "POST":
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect("curso_list")
    else:  # Método GET
        form = CursoForm(instance=curso)

    context = {"titulo": "Editar Curso", "form": form, "submit": "Actualizar Curso"}
    return render(request, "cursos/curso_form.html", context)


def delete_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    curso.delete()
    return redirect("curso_list")


def hide_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    curso.estado = "archivado"
    curso.save()

    return redirect("curso_list")


def hidden_courses(request):
    cursos = Curso.objects.select_related("categoria").filter(estado="archivado")
    cursos_data = []
    for curso in cursos:
        curso_data = {
            "id": curso.id,
            "nombre": curso.nombre,
            "descripcion": curso.descripcion,
            "precio": curso.precio,
            "fecha_publicacion": curso.fecha_publicacion,
            "categoria": curso.categoria.nombre,
            "duracion": curso.duracion,
            "num_estudiantes": curso.estudiantes.count(),
            "imagen": curso.imagen.url,
        }
        cursos_data.append(curso_data)

    context = {"cursos": cursos_data}
    return render(request, "cursos/curso_list.html", context=context)


def restore_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    curso.estado = "publicado"
    curso.save()
    return redirect("curso_list")
