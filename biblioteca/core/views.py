# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Livro, Categoria, Autor, Colecao
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer, ColecaoSerializer
from .filters import LivroFilter, CategoriaFilter, AutorFilter
from .custom_permissions import IsCollectionOwnerOrReadOnly

# Create your views here.

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']
    name = "livro-list"

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'livros': reverse('livro-list', request=request, format=format),
        'categorias': reverse('categoria-list', request=request, format=format),
        'autores': reverse('autor-list', request=request, format=format),
        'colecoes': reverse('colecao-list', request=request, format=format),
    })

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFilter
    ordering_fields = ['nome']
    name = "categoria-list"

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filterset_class = AutorFilter
    ordering_fields = ['nome']
    name = "autor-list"

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"

class ColecaoList(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    name = "colecao-list"

    def perform_create(self, serializer):
        serializer.save(colecionador=self.request.user)

class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsCollectionOwnerOrReadOnly]
    name = "colecao-detail"
