from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .serializers import UsuarioSerializer
from usuario.models import Usuario

class UsuarioCreate(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        email = serializer.validated_data['email']
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError({'code': 0, 'result': 'Email já cadastrado.'}) 
        super().perform_create(serializer)
    
    #listar todos os usuarios
class UsuarioList(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    
class  UsuarioRemove(generics.DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioListOne(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# atualizar senha
class UsuarioUpdate(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer