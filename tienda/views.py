from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.http import Http404
from datetime import date

from carro.carro import Carro

# Create your views here.


def tienda(request):

    fechaActual = date.today()

    carro = Carro(request)

    # productos = Producto.objects.all()[:5]
    # productos = Producto.objects.all().order_by('nombre')
    # productos = Producto.objects.all().order_by('-nombre')
    # productos = Producto.objects.all().order_by('id', 'nombre')
    # productos = Producto.objects.filter(categoria=1)

    # __gte es para mostrar mayor que
    # productos = Producto.objects.filter(precio__gte=500)

    # __lte es para mostrar menor que
    # productos = Producto.objects.filter(precio__lte=500)

    # productos = Producto.objects.filter(nombre__startswith='C')
    productos = Producto.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)

    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator,
        'fechaActual': fechaActual
    }

    return render(request, 'Tienda/tienda.html', data)


def redes(request):

    categorias = CategoriasProducto.objects.filter(categoria_links=2)
    

    productos = Producto.objects.all()
    

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 2)
        productos = paginator.page(page)

    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator,
        'categorias': categorias,
    }

    return render(request, 'Tienda/redes.html', data)
