import os
import django
from django.conf import settings

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto_GaleriaGZ.settings')
django.setup()

# Importar el modelo Obra
from .models import Obra

# Datos de ejemplo (simulando el JSON)
productos = [
    {
        "nombre": "Camille Pissarro",
        "descripcion": "Retrato de Paul Cézanne",
        "imagen": "static/impresionismo1.jpg",
        "precio": 2000
    },
    {
        "nombre": "Alfred Sisley",
        "descripcion": "El canal de Saint-Mammès",
        "imagen": "static/impresionismo2.jpg",
        "precio": 2500
    },
    {
        "nombre": "Mary Cassatt",
        "descripcion": "Madre e hija",
        "imagen": "static/impresionismo3.jpg",
        "precio": 2200
    },
    {
        "nombre": "Berthe Morisot",
        "descripcion": "El cuna",
        "imagen": "static/impresionismo4.jpg",
        "precio": 1800
    }
]

def importar_obras():
    for producto in productos:
        obra = Obra(
            nombre=producto['nombre'],
            descripcion=producto['descripcion'],
            precio=producto['precio'],
            imagen=producto['imagen']
        )
        obra.save()
        print(f"Obra '{obra.nombre}' importada correctamente.")

if __name__ == '__main__':
    importar_obras()