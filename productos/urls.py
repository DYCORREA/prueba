from django.urls import path
from .views import form_del_producto, form_mod_producto, form_producto , index

urlpatterns = [
    path ('' , index , name="index"),
    path ('form_producto' , form_producto , name="form_producto"),
    path ('form_mod_producto/<id>' , form_mod_producto , name="form_mod_producto"),
    path ('form_del_producto/<id>' , form_del_producto , name="form_del_producto"),
]