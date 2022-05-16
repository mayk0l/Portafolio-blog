from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def blog(request):   
    return render(request, 'core/blog.html')

def iniciarsesion(request):   
    return render(request, 'core/iniciarsesion.html')

def registro(request):   
    return render(request, 'core/registro.html')