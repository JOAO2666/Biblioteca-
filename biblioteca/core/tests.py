# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Categoria, Autor, Livro, Colecao

class ColecaoTests(APITestCase):
    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(username='user1', password='pass1234')
        self.user2 = User.objects.create_user(username='user2', password='pass1234')
        
        # Create test data
        self.categoria = Categoria.objects.create(nome='Ficcao')
        self.autor = Autor.objects.create(nome='Autor Teste')
        self.livro = Livro.objects.create(
            titulo='Livro Teste',
            autor=self.autor,
            categoria=self.categoria,
            publicado_em='2020-01-01'
        )

    def test_criar_colecao(self):
        """
        Ensure we can create a new collection when authenticated.
        """
        self.client.force_authenticate(user=self.user1)
        url = reverse('colecoes-list')
        data = {
            'nome': 'Minha Colecao',
            'descricao': 'Uma colecao de teste',
            'livros': [self.livro.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Colecao.objects.count(), 1)
        self.assertEqual(Colecao.objects.get().nome, 'Minha Colecao')

    def test_nao_pode_criar_colecao_sem_autenticacao(self):
        """
        Ensure we cannot create a collection without authentication.
        """
        url = reverse('colecoes-list')
        data = {
            'nome': 'Minha Colecao',
            'descricao': 'Uma colecao de teste',
            'livros': [self.livro.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_apenas_dono_pode_editar_colecao(self):
        """
        Ensure only the owner can edit their collection.
        """
        # Create a collection as user1
        self.client.force_authenticate(user=self.user1)
        colecao = Colecao.objects.create(
            nome='Colecao Original',
            descricao='Descricao original',
            colecionador=self.user1
        )
        colecao.livros.add(self.livro)

        # Try to edit as user2
        self.client.force_authenticate(user=self.user2)
        url = reverse('colecao-detail', kwargs={'pk': colecao.id})
        data = {
            'nome': 'Colecao Modificada',
            'descricao': 'Descricao modificada',
            'livros': [self.livro.id]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Verify the collection wasn't modified
        colecao.refresh_from_db()
        self.assertEqual(colecao.nome, 'Colecao Original')

# Create your tests here.
