from rest_framework import viewsets, status
from .models import Autor, Libro
from .serializers import AutorSerializer, LibroSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def crear_autor(request):
    if request.method == 'POST':
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def obtener_lista_autores(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['GET'])
def obtener_detalle_autor(request, autor_id):
    try:
        autor = Autor.objects.get(id=autor_id)
    except Autor.DoesNotExist:
        return Response({"error": "El autor no existe."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['PUT'])
def actualizar_autor(request, autor_id):
    try:
        autor = Autor.objects.get(id=autor_id)
    except Autor.DoesNotExist:
        return Response({"error": "El autor no existe."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def eliminar_autor(request, autor_id):
    try:
        autor = Autor.objects.get(id=autor_id)
    except Autor.DoesNotExist:
        return Response({"error": "El autor no existe."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer