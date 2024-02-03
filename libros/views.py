from django.shortcuts import render
from .models import Libros


def lista_libros(request):
    libros = Libros.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})
