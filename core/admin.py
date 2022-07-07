from django.contrib import admin
from .models import Usuario, Blog, Producto

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Blog)
admin.site.register(Producto)