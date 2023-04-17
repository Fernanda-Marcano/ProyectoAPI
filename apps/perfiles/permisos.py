from rest_framework import permissions

class UpdatePerfil(permissions.BasePermission):
    """ Le permite al usuario editar su propio perfil """
    
    def has_object_permission(self, request, view, obj):
        """ Chequear si un usuario esta editando su propio perfil """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id 
    
class UpdateStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.usuario_perfil_id == request.user.id