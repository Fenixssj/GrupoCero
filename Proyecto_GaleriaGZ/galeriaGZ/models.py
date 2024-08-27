from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

class Obra(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=50, default='Anónimo')
    categoria = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad_disponible = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    imagen = models.ImageField(upload_to='obras/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Carrito(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_agregado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.obra} - Cantidad: {self.cantidad}'

    @property
    def subtotal(self):
        return self.obra.precio * self.cantidad

class Vendido(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_vendido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.obra}'

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()

    def __str__(self):
        return f'Mensaje de {self.nombre} {self.apellido}'
