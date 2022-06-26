from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['idProducto', 'nombreProducto', 'precioProducto', 'stockProducto']
        labels ={
            'idProducto': 'ID', 
            'nombreProducto': 'Producto', 
            'precioProducto': 'Precio', 
            'stockProducto': 'Stock',
        }
        widgets={
            'idProducto': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese ID', 
                    'id': 'validationRut01',
                    'name' : "validationRut01",
                }
            ),
            'nombreProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre producto', 
                    'id': 'validationRut01',
                    'name' : "validationRut01",
                }
            ),
            'precioProducto': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese precio producto', 
                    'id': 'validationRut01',
                    'name' : "validationRut01",
                }
            ),
            'stockProducto': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese cantidad stock', 
                    'id': 'validationRut01',
                    'name' : "validationRut01",
                }
            ),
        }