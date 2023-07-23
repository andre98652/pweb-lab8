from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, LibroViewSet

# Crea un router y registra los ViewSets
router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'libros', LibroViewSet)

# Las URLs de la API están determinadas automáticamente por el router
urlpatterns = [
    path('', include(router.urls)),
]
