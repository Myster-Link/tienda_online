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
