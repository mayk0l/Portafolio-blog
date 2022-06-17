from django.urls import path
from rest_blog.views import listado_blogs, detalle_blogs
from rest_blog.viewsLogin import login

urlpatterns = [
    path('listado_blogs', listado_blogs, name="listado_blogs"),
    path('detalle_blogs/<id>',detalle_blogs,name='detalle_blogs'),
    path('login', login,name='login'),
]
