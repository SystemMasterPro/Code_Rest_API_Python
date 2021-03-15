from rest_framework import serializers
from .models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields= '__all__'

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model= Almacen
        fields= '__all__'