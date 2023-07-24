from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Crea un router y registra los ViewSets
router = DefaultRouter()
router.register(r'autores-api', AutorViewSet)
router.register(r'libros-api', LibroViewSet)

# Las URLs de la API estan determinadas automaticamente por el router
urlpatterns = [
    path('', include(router.urls)),
    path('libros/lista/', obtener_lista_libros, name='lista_libros'),
    path('libros/nuevo/', crear_libro, name='crear_libro'),
    path('libros/<int:libro_id>/', obtener_detalle_libro, name='detalle_libro'),
    path('libros/<int:libro_id>/actualizar/', actualizar_libro, name='actualizar_libro'),
    path('autores/lista/', obtener_lista_autores, name='lista_autores'),
    path('autores/<int:autor_id>/', obtener_detalle_autor, name='detalle_autor'),
    path('autores/nuevo/', crear_autor, name='crear_autor'),
    path('autores/<int:autor_id>/actualizar/', actualizar_autor, name='actualizar_autor'),
    path('autores/<int:autor_id>/eliminar/', eliminar_autor, name='eliminar_autor'),
]
