from django.shortcuts import render


def home(request):
    return render(
        request,
        "base.html",
        context={"li_01": "HOME", "li_02": "CURSOS", "li_03": "estudiantes"},
    )
