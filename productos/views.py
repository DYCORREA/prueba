from math import prod
from django.shortcuts import render , redirect

from productos.forms import ProductoForm
from .models import Producto

# Create your views here.
def index (request):
    productos = Producto.objects.all()
    datos = {
        'productos' : productos
    }

    return render(request , 'index.html' , datos)

# def form_producto (request):
#     return render(request , 'form_producto.html')

def form_producto(request):
    if request.method=='POST': 
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form= ProductoForm()
    return render(request, 'form_producto.html', {'form': form})

def form_mod_producto(request , id):

    producto = Producto.objects.get (idProducto = id)

    datos = {
        'form' : ProductoForm (instance= producto)
    }

    if (request.method == 'POST'):
        formulario = ProductoForm(data=request.POST , instance= producto)
        if (formulario.is_valid):
            formulario.save()
            return redirect('index')

    return render(request, 'form_mod_prod.html' , datos)


def form_del_producto(request , id):

    producto = Producto.objects.get (idProducto = id)

    producto.delete()

    return redirect('index')