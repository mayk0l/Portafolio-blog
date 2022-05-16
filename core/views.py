from django.shortcuts import render
from .models import Blog

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def blog(request):   
    return render(request, 'core/blog.html')

def iniciarsesion(request):   
    return render(request, 'core/iniciarsesion.html')

def registro(request):   
    return render(request, 'core/registro.html')

def listadoblogs(request):
    blogs = Blog.objects.all()
    datos = {
        'blogs':blogs
    }
    return render(request, 'core/listadoblogs.html',datos)