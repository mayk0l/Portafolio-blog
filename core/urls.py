from django.urls import path
from .views import eliminar_blog, home, blog, iniciarsesion, registro, listadoblogs, form_blog, modificar_blog, agregar_producto, descontar_producto, restar_producto, limpiar_carrito
urlpatterns = [
    path('', home,name="home"),
    path('blog/', blog,name="blog"),
    path('iniciarsesion/', iniciarsesion,name="iniciarsesion"),
    path('registro/', registro,name="registro"),
    path('listadoblogs/', listadoblogs,name="listadoblogs"),
    path('form_blog/', form_blog,name="form_blog"),
    path('modificar_blog/<id>', modificar_blog,name='modificar_blog'),
    path('eliminar_blog/<id>', eliminar_blog,name='eliminar_blog'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', descontar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]