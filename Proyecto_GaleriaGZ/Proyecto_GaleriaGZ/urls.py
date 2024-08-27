from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from galeriaGZ.views import ( 
    inicio_view, login_view, categoria_view, contacto_view, 
    ingresar_obra_view, nosotros_view, registro_view, perfil_view, 
    perfil_artista_view, perfil_obra_view, galeria1_impresionismo_view,
    galeria2_cubismo_view, galeria3_surrealismo_view, galeria4_abstracto_view,
    carrito_de_compras, custom_logout_view, contacto_exitoso, comprar_obra, eliminar_del_carrito, confirmar_compra,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_view, name='inicio'),
    path('login/', login_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', custom_logout_view, name='logout'),
    path('categoria/', categoria_view, name='categoria'),
    path('contacto/', contacto_view, name='contacto'),
    path('ingresar_obra/', ingresar_obra_view, name='ingresar_obra'),
    path('nosotros/', nosotros_view, name='nosotros'),
    path('registro/', registro_view, name='registro'),
    path('perfil/', perfil_view, name='perfil'),
    path('perfil_artista/', perfil_artista_view, name='perfil_artista'),
    path('perfil_obra/', perfil_obra_view, name='perfil_obra'),
    path('galeria1_impresionismo/', galeria1_impresionismo_view, name='galeria1_impresionismo'),
    path('galeria2_cubismo/', galeria2_cubismo_view, name='galeria2_cubismo'),
    path('galeria3_surrealismo/', galeria3_surrealismo_view, name='galeria3_surrealismo'),
    path('galeria4_abstracto/', galeria4_abstracto_view, name='galeria4_abstracto'),
    path('comprar/<int:obra_id>/', comprar_obra, name='comprar_obra'),
    path('carrito/', carrito_de_compras, name='carrito_de_compras'),
    path('eliminar_del_carrito/<int:obra_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('confirmar_compra/', confirmar_compra, name='confirmar_compra'),
    path('contacto_exitoso/', contacto_exitoso, name='contacto_exitoso'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
