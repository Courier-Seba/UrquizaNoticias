from django.db import models

# Create your models here.

class Aviso(models.Model):
    titulo = models.CharField()
    descripcion = models.TextField()
    contacto = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

