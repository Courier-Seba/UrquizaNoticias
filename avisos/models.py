from django.db import models

# Create your models here.

class Aviso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    contacto = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

