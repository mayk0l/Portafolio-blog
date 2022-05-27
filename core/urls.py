from django.urls import path
from .views import eliminar_blog, home, blog, iniciarsesion, registro, listadoblogs, form_blog, modificar_blog
urlpatterns = [
    path('', home,name="home"),
    path('blog/', blog,name="blog"),
    path('iniciarsesion/', iniciarsesion,name="iniciarsesion"),
    path('registro/', registro,name="registro"),
    path('listadoblogs/', listadoblogs,name="listadoblogs"),
    path('form_blog/', form_blog,name="form_blog"),
    path('modificar_blog/<id>', modificar_blog,name='modificar_blog'),
    path('eliminar_blog/<id>', eliminar_blog,name='eliminar_blog'),
]