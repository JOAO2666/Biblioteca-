from django.conf.urls import url
from rest_framework.authtoken import views as token_views
from . import views

urlpatterns = [
    url(r'^$', views.api_root, name='api-root'),
    url(r'^livros/$', views.LivroList.as_view(), name='livro-list'),
    url(r'^livros/(?P<pk>[0-9]+)/$', views.LivroDetail.as_view(), name='livro-detail'),
    url(r'^categorias/$', views.CategoriaList.as_view(), name='categoria-list'),
    url(r'^categorias/(?P<pk>[0-9]+)/$', views.CategoriaDetail.as_view(), name='categoria-detail'),
    url(r'^autores/$', views.AutorList.as_view(), name='autor-list'),
    url(r'^autores/(?P<pk>[0-9]+)/$', views.AutorDetail.as_view(), name='autor-detail'),
    url(r'^colecoes/$', views.ColecaoList.as_view(), name='colecao-list'),
    url(r'^colecoes/(?P<pk>[0-9]+)/$', views.ColecaoDetail.as_view(), name='colecao-detail'),
    url(r'^api-token-auth/$', token_views.obtain_auth_token, name='api-token'),
]
