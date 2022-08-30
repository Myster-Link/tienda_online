from xmlrpc.client import boolean
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CategoriasLinks(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'categoria_link'
        verbose_name_plural = 'categorias_links'

    def __str__(self):
        return self.nombre


class CategoriasProducto(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    categoria_links = models.ManyToManyField(CategoriasLinks)

    class Meta:
        verbose_name = 'categoria_producto'
        verbose_name_plural = 'categorias_productos'

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    codigo_producto = models.CharField(max_length=30, unique=True)
    stock = models.IntegerField()
    precio = models.FloatField()
    descripcion = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    categoria = models.ForeignKey(
        CategoriasProducto, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.SET_NULL, null=True)
    destacados_semanales = models.BooleanField(null=True)
    producto_nuevo = models.BooleanField(null=True)
    oferta = models.BooleanField(null=True)
    precio_descuento = models.FloatField(null=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return f'Nombre: {self.nombre}, Stock: {self.stock},  Precio: {self.precio}, Oferta: {self.oferta}'
