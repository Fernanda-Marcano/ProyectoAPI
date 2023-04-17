from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, UsuarioLoginApiView, UsuarioPerfilFeedView

router = DefaultRouter()
router.register('perfil', UsuarioViewSet)
router.register('perfilfeed', UsuarioPerfilFeedView, basename='perfil')



urlpatterns = [
    path('login/', UsuarioLoginApiView.as_view()),
    path('', include(router.urls)),
]