from rest_framework import serializers
from .models import Filme

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['id', 'nome', 'descricao', 'genero', 'diretor', 'ano']
