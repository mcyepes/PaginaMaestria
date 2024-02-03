from django.db import models


class Libros(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    resumen = models.TextField()

    def __str__(self):
        return self.titulo
