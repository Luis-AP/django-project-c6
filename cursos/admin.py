from django.contrib import admin

from .models import Curso, Categoria, Instructor, Estudiante, Inscripcion
from tinymce.widgets import TinyMCE

from django.db.models import TextField


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "precio",
        "fecha_publicacion",
        "categoria",
        "instructor",
    )
    search_fields = ("nombre", "descripcion", "categoria__nombre", "instructor__nombre")
    list_filter = ("categoria", "estado", "fecha_publicacion")
    ordering = ("nombre", "precio", "fecha_publicacion")
    fieldsets = (
        (
            "Información general",
            {"fields": ("nombre", "descripcion", "precio", "fecha_publicacion")},
        ),
        (
            "Detalles del curso",
            {
                "fields": (
                    "categoria",
                    "instructor",
                    "duracion",
                    "estado",
                    "destacado",
                    "requisitos",
                    "imagen",
                    "contenido",
                )
            },
        ),
    )
    formfield_overrides = {
        TextField: {"widget": TinyMCE()},
    }


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "color")
    search_fields = ("nombre",)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "bio")
    search_fields = ("nombre",)


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email")
    search_fields = ("nombre", "email")


admin.site.register(Inscripcion)
