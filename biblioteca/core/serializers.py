from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Categoria, Autor, Livro, Colecao

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome']

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'categoria', 'publicado_em']

class ColecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colecao
        fields = ['id', 'nome', 'descricao', 'livros', 'colecionador']
        read_only_fields = ['colecionador']

    def create(self, validated_data):
        validated_data['colecionador'] = self.context['request'].user
        return super(ColecaoSerializer, self).create(validated_data)
