from django.shortcuts import render
from .models import Blog
from .forms import BlogForm

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

def agregarblog(request):
    datos = {
        'form' : BlogForm()
    }

    if (request.method == 'POST'):
        formulario = BlogForm(request.POST)
        if formulario.is_valid():
            formulario.save() #insert
            datos['mensaje'] = "Se guardó blog"
        else:
            datos['mensaje'] = "Revise datos"
    return render(request, 'core/agregarblog.html',{'datos':datos})