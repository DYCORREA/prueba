from django.db import models

# Create your models here.

class Producto (models.Model):
    idProducto = models.IntegerField( primary_key=True , verbose_name= 'ID PRODUCTO' )
    nombreProducto = models.CharField(max_length= 100 ,  verbose_name= 'NOMBRE PRODUCTO' )
    precioProducto = models.IntegerField( verbose_name= 'PRECIO PRODUCTO' )
    stockProducto = models.IntegerField( verbose_name= 'STOCK PRODUCTO' )
    
    def __str__(self):
        return self.nombreProducto
