from django.shortcuts import render, redirect, HttpResponse
from .models import Blog
from .forms import BlogForm

# Create your views here.
from core.models import Producto
from core.Carrito import Carrito

def home(request):
    productos = Producto.objects.all()
    return render(request, 'core/home.html', {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("home")

def descontar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("home")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("home")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("home")

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