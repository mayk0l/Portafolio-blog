from django.shortcuts import render, redirect
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

def form_blog(request):
    datos = {
        'form' : BlogForm()
    }

    if (request.method == 'POST'):
        formulario = BlogForm(request.POST)
        if formulario.is_valid():
            formulario.save() 
            datos['mensaje'] = "Se guardó el blog"
    return render(request, 'core/form_blog.html', datos)

def modificar_blog(request, id):
    blogs = Blog.objects.get(idBlog=id)

    datos = {
        'form' : BlogForm(instance=blogs)
    }

    if (request.method == 'POST'):
        formulario = BlogForm(data = request.POST, instance = blogs)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Se modificó blog"

    return render(request,'core/modificar_blog.html', datos)

def eliminar_blog(request, id):
    blogs = Blog.objects.get(idBlog=id)
    blogs.delete()

    return redirect(to='home')