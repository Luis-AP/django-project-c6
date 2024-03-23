from django.db import models
from datetime import timedelta


class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField()


class Estudiante(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=20)


class Curso(models.Model):
    nombre = models.CharField(max_length=10)
    descripcion = models.TextField()
    precio = models.IntegerField()
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    duracion = models.DurationField(default=timedelta(days=0))
    estado = models.CharField(
        max_length=20,
        choices=[
            ("borrador", "Borrador"),
            ("publicado", "Publicado"),
            ("archivado", "Archivado"),
        ],
        help_text="Los estados de curso pueden ser: Borrador, Publicado o Archivado",
    )
    requisitos = models.TextField(blank=True)
    destacado = models.BooleanField(default=False)
    instructor = models.ForeignKey(
        Instructor, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.nombre
