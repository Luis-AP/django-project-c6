from django.contrib import admin

from .models import Curso, Categoria, Instructor, Estudiante


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "fecha_publicacion", "categoria", "instructor")
    search_fields = ("nombre", "descripcion", "categoria__nombre", "instructor__nombre")
    ordering = ("nombre", "precio", "fecha_publicacion")
    list_filter = ("categoria", "instructor", "destacado")


admin.site.register(Categoria)
admin.site.register(Instructor)
admin.site.register(Estudiante)
