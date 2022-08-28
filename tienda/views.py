from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.


def tienda(request):

    productos = Producto.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 20)
        productos = paginator.page(page)

    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }

    return render(request, 'Tienda/tienda.html', data)
