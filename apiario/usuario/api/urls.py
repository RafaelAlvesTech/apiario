from django.urls import path
from .views import UsuarioCreate, UsuarioList, UsuarioListOne, UsuarioRemove, UsuarioUpdate


urlpatterns = [
    path('criar_usuario/', UsuarioCreate.as_view()),
    path('listar_usuarios/', UsuarioList.as_view()),
    path('listar_um_usuario/<int:id>/', UsuarioListOne.as_view()),
    path('remover_usuario/<int:id>/', UsuarioRemove.as_view()),
    path('atualizar_usuario/<int:id>/', UsuarioUpdate.as_view())

]
