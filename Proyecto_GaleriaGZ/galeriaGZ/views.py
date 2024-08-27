from django.shortcuts import render, redirect, get_object_or_404
from .models import Obra, Carrito, Vendido, Contacto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import UserRegistrationForm, ContactoForm
from django.utils import timezone
from django.contrib import messages

# Aca esta lo mas inportante del HTML:
def inicio_view(request):
    return render(request, "inicio.html")

def categoria_view(request):
    return render(request, "categoria.html")

def contacto_view(request):
    return render(request, "contacto.html")

def nosotros_view(request):
    return render(request, "nosotros.html")

def perfil_artista_view(request):
    return render(request, "perfil_artista.html")

def perfil_obra_view(request):
    return render(request, "perfil-obra.html")

# ACA VAMOS A LLAMAR TDODA LA GALERIA PARA QUE LA PAGINA FUNCIONE:

def galeria1_impresionismo_view(request):
    obras = Obra.objects.filter(categoria='Impresionismo')
    return render(request, 'galeria1_impresionismo.html', {'obras': obras})

def galeria2_cubismo_view(request):
    obras = Obra.objects.filter(categoria='Cubismo')
    return render(request, 'galeria2_cubismo.html', {'obras': obras})

def galeria3_surrealismo_view(request):
    obras = Obra.objects.filter(categoria='Surrealismo')
    return render(request, 'galeria3_surrealismo.html', {'obras': obras})

def galeria4_abstracto_view(request):
    obras = Obra.objects.filter(categoria='Abstracto')
    return render(request, 'galeria4_abstracto.html', {'obras': obras})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            
            return render(request, 'registration/login.html', {'error_message': 'Credenciales incorrectas'})
    else:
        return render(request, 'registration/login.html')
    

def contacto_views(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contacto.html', {'form': ContactoForm(), 'success': True})
        else:
            return render(request, 'contacto.html', {'form': form})
    else:
        form = ContactoForm()
    
    return render(request, 'contacto.html', {'form': form})

def contacto_exitoso(request):
    return render(request, 'contacto_exitoso.html')

def custom_logout_view(request):
    logout(request)
    return redirect('/')

def registro_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserRegistrationForm()
    return render(request, 'registro.html', {'form': form})

@login_required

def ingresar_obra_view(request):
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES)
        if form.is_valid():
            nombre_nueva_obra = form.cleaned_data['nombre']
            obra_existente = Obra.objects.filter(nombre=nombre_nueva_obra).first()
            
            if obra_existente:
                 obra_existente.cantidad_disponible += 1
                 obra_existente.save()
            else:
                obra_nueva = form.save(commit=False)
                obra_nueva.save()
            return redirect('ingresar_obra')  
    else:
        form = ObraForm()
    
    return render(request, 'ingresar_obra.html', {'form': form})

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['nombre', 'autor', 'categoria', 'precio', 'imagen']

def perfil_view(request):
    return render(request, "perfil.html")

def comprar_obra(request, obra_id):
    obra = get_object_or_404(Obra, pk=obra_id)

    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))

        if cantidad <= 0:
            messages.error(request, "La cantidad debe ser mayor que cero.")
        elif cantidad > obra.cantidad_disponible:
            messages.error(request, f"No hay suficiente stock disponible para '{obra.nombre}'.")
        else:
            carrito, created = Carrito.objects.get_or_create(
                obra=obra,
                defaults={'cantidad': cantidad}
            )

            if not created:
                carrito.cantidad += cantidad
                carrito.save()

            messages.success(request, f"Se ha agregado '{obra.nombre}' al carrito.")

            return redirect('carrito_de_compras')

        return redirect('comprar_obra', obra_id=obra_id)

    context = {
        'obra': obra
    }
    return render(request, 'comprar_obra.html', context)


def carrito_de_compras(request):
    carrito = Carrito.objects.all()
    total = sum(item.subtotal for item in carrito)
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})

def eliminar_del_carrito(request, obra_id):
    carrito = get_object_or_404(Carrito, obra_id=obra_id)
    obra = carrito.obra    
    carrito.delete()
    
    return redirect('carrito_de_compras')

def confirmar_compra(request):
    if request.method == 'POST' and 'confirmar' in request.POST:
        carrito_items = Carrito.objects.all()
        for item in carrito_items:
            Vendido.objects.create(
                obra=item.obra,
                cantidad=item.cantidad,
                fecha_vendido=timezone.now()
            )
            item.obra.cantidad_disponible -= item.cantidad
            item.obra.save()
        Carrito.objects.all().delete()
        return redirect('inicio')
    else:
        carrito_items = Carrito.objects.all()
        total = sum(item.subtotal for item in carrito_items)
        return render(request, 'confirmar_compra.html', {'carrito': carrito_items, 'total': total})