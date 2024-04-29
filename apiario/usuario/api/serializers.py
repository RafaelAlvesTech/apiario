from rest_framework import serializers
from usuario.models import UsuarioCreate

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCreate
        fields = '__all__'