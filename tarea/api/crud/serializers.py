from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Autor, Libro

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'