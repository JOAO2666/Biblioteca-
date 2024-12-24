# Biblioteca - Library Management System

A Django-based Library Management System with REST API support, featuring book collections, user authentication, and automated testing.

## Features

- **Book Management**
  - Create, read, update, and delete books
  - Associate books with authors and categories
  - Search and filter books by various criteria

- **Collection Management**
  - Users can create personal book collections
  - Add/remove books to/from collections
  - Collections are private to their owners
  - Full CRUD operations for collections

- **Authentication & Authorization**
  - Token-based authentication
  - Permission-based access control
  - Secure API endpoints
  - User-specific collection management

- **API Endpoints**
  - `/` - API root with endpoint navigation
  - `/livros/` - Book management
  - `/autores/` - Author management
  - `/categorias/` - Category management
  - `/colecoes/` - Collection management
  - `/api-token-auth/` - Token authentication

## Technology Stack

- Python 2.7 (Legacy support)
- Django
- Django REST Framework
- SQLite Database
- Token Authentication

## Installation

1. Clone the repository:
```bash
git clone https://github.com/JOAO2666/Biblioteca-.git
cd Biblioteca
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

5. Start the development server:
```bash
python manage.py runserver
```

## API Usage

### Authentication

To use protected endpoints, obtain an authentication token:

```bash
curl -X POST http://localhost:8000/api-token-auth/ -d "username=your_username&password=your_password"
```

Use the token in subsequent requests:

```bash
curl -H "Authorization: Token your_token_here" http://localhost:8000/colecoes/
```

### Collections

- Create a collection:
```bash
curl -X POST http://localhost:8000/colecoes/ -H "Authorization: Token your_token" -d "nome=My Collection&descricao=Description"
```

- List collections:
```bash
curl -H "Authorization: Token your_token" http://localhost:8000/colecoes/
```

## Testing

Run the test suite:

```bash
python manage.py test
```

Or with coverage:

```bash
coverage run manage.py test
coverage report
```

## Project Structure

- `biblioteca/` - Main project directory
  - `core/` - Main application
    - `models.py` - Database models
    - `views.py` - API views
    - `serializers.py` - REST framework serializers
    - `urls.py` - URL routing
    - `tests.py` - Test cases
    - `custom_permissions.py` - Custom permission classes

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Future Improvements

- Upgrade to Python 3.x
- Add more comprehensive test coverage
- Implement book borrowing system
- Add user profiles and ratings
- Integrate with external book APIs
- Add frontend interface
