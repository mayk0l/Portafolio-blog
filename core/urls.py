from django.urls import path
from .views import home, blog, iniciarsesion, registro

urlpatterns = [
    path('', home,name="home"),
    path('blog/', blog,name="blog"),
    path('iniciarsesion/', iniciarsesion,name="iniciarsesion"),
    path('registro/', registro,name="registro"),
]