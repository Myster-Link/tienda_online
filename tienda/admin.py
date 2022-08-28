from django.contrib import admin
from .models import *

# Register your models here.

class CamposDate(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')



admin.site.register(CategoriasProducto, CamposDate)
admin.site.register(Proveedor, CamposDate)
admin.site.register(Producto, CamposDate)
