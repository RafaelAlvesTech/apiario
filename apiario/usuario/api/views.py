from rest_framework import generics
from .serializers import UsuarioSerializer
from usuario.models import Usuario



class UsuarioCreate(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
 # email validation
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        if Usuario.objects.filter(email=email).exists():
            return Response({'code': 0, 'result': 'Email já cadastrado.'}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'code': 1, 'result': 'Usuário cadastrado com sucesso.'}, status=status.HTTP_201_CREATED, headers=headers)
