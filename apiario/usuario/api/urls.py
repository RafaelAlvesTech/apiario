from django.urls import path
from .views import UsuarioCreate, UsuarioList, UsuarioListOne, UsuarioRemove, UsuarioUpdate


urlpatterns = [
    path('criar_usuario/', UsuarioCreate.as_view()),
    path('listar_usuarios/', UsuarioList.as_view()),
    path('listar_um_usuario/<int:pk>/', UsuarioListOne.as_view()),
    path('remover_usuario/<int:pk>/', UsuarioRemove.as_view()),
    path('atualizar_usuario/<int:pk>/', UsuarioUpdate.as_view()),
    path ('atualizar_senha/<str:pk>/', UsuarioUpdate.as_view()),
]
