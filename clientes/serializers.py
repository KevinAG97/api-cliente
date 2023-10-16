from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF inválido."})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O nome deve ter apenas caracteres alfabéticos!"})
        
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'RG':"O RG deve ter 9 dígitos!"})
        
        if not validate_celular(data['celular']):
            raise serializers.ValidateError({'Celular':"O número de celular deve seguir este modelo: xx xxxxx-xxxx"})
        
        return data


    '''
    def validate_rg(self, rg):
        if len(rg) !=9:
            raise serializers.ValidationError("O RG deve ter 9 dígitos!")
        return rg
    def validate_celular(self, celular):
        if len(celular) < 11:
            raise serializers.ValiationError("O Campo deve conter 11 dígitos!")
        return celular'''