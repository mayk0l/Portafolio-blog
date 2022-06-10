from django.urls import path
from rest_blog.views import listado_blogs, detalle_blogs

urlpatterns = [
    path('listado_blogs', listado_blogs, name="listado_blogs"),
    path('detalle_blogs/<id>',detalle_blogs,name='detalle_blogs'),
]
