from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# Creacion de modelo. Usuario personalizado

class UsuarioManager(BaseUserManager):
    """ Manager para el perfil de usuario """
    def create_user(self, email, username, nombres, apellidos, password=None):
        """ Funcion de usuario """
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        email = self.normalize_email(email)
        usuario = self.model(email=email, username=username, nombres=nombres, apellidos=apellidos)
        
        usuario.set_password(password)
        usuario.save(using=self._db)
        
        return usuario
    
    def create_superuser(self, email, username, nombres, apellidos, password):
        """ Funcion de super usuario """
        usuario = self.create_user(email, username, nombres, apellidos, password)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save(using=self._db)
        
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    """ Modelo de usuario para la base de datos """
    username = models.CharField(verbose_name='Nombre de usuario', max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(verbose_name='Correo electrónico', max_length=150, unique=True, null=False, blank=False)
    nombres = models.CharField(verbose_name='Nombres', max_length=200, null=False, blank=False)
    apellidos = models.CharField(verbose_name='Apellidos', max_length=200, null=False, blank=False)
    status = models.BooleanField(verbose_name='Estado', default=True)
    is_staff = models.BooleanField(default=False)
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']
    
    def get_full_name(self):
        """ Mostrar nombre completo del usuaio """
        return self.nombres
    
    def get_short_name(self):
        return self.nombres
    
    def __str__(self):
        """ Retornar cadena del usuario """
        return f'{self.nombres}, {self.apellidos}'
    
    
class PerfilFeed(models.Model):
    """ Perfil de status update """
    usuaro_perfil = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=200)
    created_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.status_text