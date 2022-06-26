# Generated by Django 4.0.4 on 2022-06-25 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID PRODUCTO')),
                ('nombreProducto', models.CharField(max_length=100, verbose_name='NOMBRE PRODUCTO')),
                ('precioProducto', models.IntegerField(verbose_name='PRECIO PRODUCTO')),
                ('stockProducto', models.IntegerField(verbose_name='STOCK PRODUCTO')),
            ],
        ),
    ]
