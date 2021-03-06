from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=20, null=False, blank=False)
    apellidos = models.CharField(max_length=20, null=False, blank=False)
    nombreUsuario = models.CharField(max_length=20, null=False, blank=False)
    contrasenaUsuario = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.nombreUsuario


class Blog(models.Model):
    idBlog = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=20, null=False, blank=False)
    body = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'