from rest_framework import serializers
from .models import Usuario, UsuarioManager, PerfilFeed

class UsuarioSerializer(serializers.ModelSerializer):
    """ Serializa el objeto de perfil de usuario """   
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'nombres', 'apellidos', 'password', 'status', 'is_staff')
        extra_kwargs = {
            'password':{
                #* Esto nos ayuda a que nuestra clase solo se vea cuando se esta creando
                'write_only': True,
                #? Con style, protegemos la contrasena y hacemos que aparezca encriptada
                'style': {'input_type':'password'}
            }
        }
        
    def create(self, validated_data):
        """ Crear nuevos usuarios en la base de datos """
        usuario = Usuario.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            nombres = validated_data['nombres'], 
            apellidos = validated_data['apellidos'],
            password = validated_data['password']
        )
        return usuario
    
    def update(self, instance, validated_data):
        """ Actualizacion de usuarios """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
    
class PerfilFeedSerializer(serializers.ModelSerializer):
    """ Serializador de perfil feed """
    
    class Meta:
        model = PerfilFeed
        fields = ('id', 'usuario_perfil', 'status_text', 'created_on')
        extra_kwargs = {'usuario_perfil':{'read_only':True}}