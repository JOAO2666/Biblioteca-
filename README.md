# Sistema de Gerenciamento de Biblioteca

Um sistema de gerenciamento de biblioteca baseado em Django com suporte a API REST, apresentando coleções de livros, autenticação de usuários e testes automatizados.

## Funcionalidades

- **Gerenciamento de Livros**
  - Criar, ler, atualizar e excluir livros
  - Associar livros a autores e categorias
  - Pesquisar e filtrar livros por diversos critérios

- **Gerenciamento de Coleções**
  - Usuários podem criar coleções pessoais de livros
  - Adicionar/remover livros das coleções
  - Coleções são privadas para seus proprietários
  - Operações completas de CRUD para coleções

- **Autenticação e Autorização**
  - Autenticação baseada em token
  - Controle de acesso baseado em permissões
  - Endpoints de API seguros
  - Gerenciamento de coleções específico por usuário

- **Endpoints da API**
  - `/` - Raiz da API com navegação de endpoints
  - `/livros/` - Gerenciamento de livros
  - `/autores/` - Gerenciamento de autores
  - `/categorias/` - Gerenciamento de categorias
  - `/colecoes/` - Gerenciamento de coleções
  - `/api-token-auth/` - Autenticação por token

## Tecnologias Utilizadas

- Python 2.7 (Suporte legado)
- Django
- Django REST Framework
- Banco de dados SQLite
- Autenticação por Token

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/JOAO2666/Biblioteca-.git
cd Biblioteca
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute as migrações:
```bash
python manage.py migrate
```

4. Crie um superusuário (opcional):
```bash
python manage.py createsuperuser
```

5. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

## Uso da API

### Autenticação

Para usar endpoints protegidos, obtenha um token de autenticação:

```bash
curl -X POST http://localhost:8000/api-token-auth/ -d "username=seu_usuario&password=sua_senha"
```

Use o token nas requisições subsequentes:

```bash
curl -H "Authorization: Token seu_token_aqui" http://localhost:8000/colecoes/
```

### Coleções

- Criar uma coleção:
```bash
curl -X POST http://localhost:8000/colecoes/ -H "Authorization: Token seu_token" -d "nome=Minha Coleção&descricao=Descrição"
```

- Listar coleções:
```bash
curl -H "Authorization: Token seu_token" http://localhost:8000/colecoes/
```

## Testes

Execute a suite de testes:

```bash
python manage.py test
```

Ou com cobertura:

```bash
coverage run manage.py test
coverage report
```

## Estrutura do Projeto

- `biblioteca/` - Diretório principal do projeto
  - `core/` - Aplicação principal
    - `models.py` - Modelos do banco de dados
    - `views.py` - Views da API
    - `serializers.py` - Serializadores do REST framework
    - `urls.py` - Roteamento de URLs
    - `tests.py` - Casos de teste
    - `custom_permissions.py` - Classes de permissões personalizadas

## Como Contribuir

1. Faça um fork do repositório
2. Crie sua branch de feature (`git checkout -b feature/NovaFuncionalidade`)
3. Faça commit de suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

## Melhorias Futuras

- Atualização para Python 3.x
- Adicionar mais cobertura de testes
- Implementar sistema de empréstimo de livros
- Adicionar perfis de usuário e avaliações
- Integrar com APIs externas de livros
- Adicionar interface frontend
