from django.urls import path
from .views import UsuarioCreate


urlpatterns = [
    path('usuario/', UsuarioCreate.as_view())
]
