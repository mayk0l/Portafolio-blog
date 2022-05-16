from django.urls import path
from .views import home, blog, iniciarsesion, registro, listadoblogs

urlpatterns = [
    path('', home,name="home"),
    path('blog/', blog,name="blog"),
    path('iniciarsesion/', iniciarsesion,name="iniciarsesion"),
    path('registro/', registro,name="registro"),
    path('listadoblogs/', listadoblogs,name="listadoblogs"),
]