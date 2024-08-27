from django.contrib import admin

from .models import Obra, Carrito, Vendido, Contacto

# Register your models here.
admin.site.register(Obra)
admin.site.register(Carrito)
admin.site.register(Vendido)
admin.site.register(Contacto)


