from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets, request
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from .serializers import UsuarioSerializer, PerfilFeedSerializer
from .models import Usuario, PerfilFeed
from .permisos import UpdatePerfil,UpdateStatus

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    """ Crear y actualizar perfiles """
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdatePerfil,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'nombres',)
    
    def destroy(self, request, pk=None):
        return Response({'http_method':'DELETE'})
    
class UsuarioLoginApiView(ObtainAuthToken):
    """ Crea tokens de autenticacion de usuario """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class UsuarioPerfilFeedView(viewsets.ModelViewSet):
    """ Feed que maneja el crear, leer y actualizar """
    authentication_classes = (TokenAuthentication,)
    serializer_class = PerfilFeedSerializer
    queryset = PerfilFeed.objects.all()
    permission_classes = (UpdateStatus, IsAuthenticated)
    
    def perform_create(self, serializer):
        serializer.save(usuario_perfil=self.request.user)