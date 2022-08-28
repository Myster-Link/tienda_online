from django.shortcuts import render
from .models import *

# Create your views here.

def tienda(request):

    categorias = CategoriasProducto.objects.all()
    productos = Producto.objects.all()

    return render(request, 'Tienda/tienda.html', {'productos':productos, 'categorias':categorias})