from django.db import models

# Create your models here.


class CategoriasProducto(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'categoria_producto'
        verbose_name_plural = 'categorias_producto'

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
    # id_user =
    nombre = models.CharField(max_length=30)
    codigo_producto = models.CharField(max_length=30)
    categoria = models.ForeignKey(
        CategoriasProducto, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.SET_NULL, null=True)
    stock = models.IntegerField()
    precio = models.FloatField()
    descripcion = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return f'Nombre: {self.nombre}, Stock: {self.stock},  Precio: {self.precio}'
