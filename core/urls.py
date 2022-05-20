from django.urls import path
from .views import home, blog, iniciarsesion, registro, listadoblogs, agregarblog

urlpatterns = [
    path('', home,name="home"),
    path('blog/', blog,name="blog"),
    path('iniciarsesion/', iniciarsesion,name="iniciarsesion"),
    path('registro/', registro,name="registro"),
    path('listadoblogs/', listadoblogs,name="listadoblogs"),
    path('agregarblog/', agregarblog,name="agregarblog"),
]