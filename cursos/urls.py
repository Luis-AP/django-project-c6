from django.urls import path

from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("cursos/", curso_list, name="curso_list"),
    path("cursos/<int:curso_id>/", curso_detail, name="curso_detail"),
    path("cursos/crear/", create_curso, name="curso_create"),
    path("cursos/<int:curso_id>/actualizar/", update_curso, name="curso_update"),
    path("cursos/<int:curso_id>/eliminar/", delete_curso, name="curso_delete"),
    path("cursos/<int:curso_id>/archivar/", hide_curso, name="hide_curso"),
    path("cursos/ocultos/", hidden_courses, name="hidden_courses"),
    path("cursos/<int:curso_id>/restaurar/", restore_curso, name="restore_curso"),
]
