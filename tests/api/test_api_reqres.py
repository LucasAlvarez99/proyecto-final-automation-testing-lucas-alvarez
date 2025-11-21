"""
Pruebas de API - ReqRes
=======================

Este módulo contiene pruebas automatizadas para la API pública ReqRes.
Cubre métodos GET, POST y DELETE con validaciones de respuesta.

Nota: ReqRes ahora requiere API key. Se usa la key gratuita 'reqres-free-v1'.
"""

import requests

BASE_URL = "https://reqres.in/api"

# Headers requeridos por ReqRes (API key gratuita)
HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": "reqres-free-v1"
}


class TestReqResAPI:
    """Suite de pruebas para la API de ReqRes."""

    def test_get_lista_usuarios(self):
        """
        GET /users - Obtener lista paginada de usuarios.
        
        Verifica:
        - Status code 200
        - Respuesta contiene campo 'data'
        - 'data' es una lista con usuarios
        """
        response = requests.get(
            f"{BASE_URL}/users?page=2",
            headers=HEADERS
        )
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        body = response.json()
        assert "data" in body, "Response should contain 'data' field"
        assert isinstance(body["data"], list), "'data' should be a list"
        assert len(body["data"]) > 0, "Users list should not be empty"
        
        # Verificar estructura de un usuario
        first_user = body["data"][0]
        assert "id" in first_user
        assert "email" in first_user
        assert "first_name" in first_user

    def test_get_usuario_individual(self):
        """
        GET /users/{id} - Obtener un usuario específico.
        
        Verifica:
        - Status code 200
        - Respuesta contiene datos del usuario
        """
        response = requests.get(
            f"{BASE_URL}/users/2",
            headers=HEADERS
        )
        
        assert response.status_code == 200
        
        body = response.json()
        assert "data" in body
        assert body["data"]["id"] == 2

    def test_crear_usuario(self):
        """
        POST /users - Crear un nuevo usuario.
        
        Verifica:
        - Status code 201 (Created)
        - Respuesta contiene los datos enviados
        - Respuesta incluye 'id' y 'createdAt' generados
        """
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        
        response = requests.post(
            f"{BASE_URL}/users",
            json=payload,
            headers=HEADERS
        )
        
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        
        data = response.json()
        assert data.get("name") == "morpheus"
        assert data.get("job") == "leader"
        assert "id" in data, "Response should contain generated 'id'"
        assert "createdAt" in data, "Response should contain 'createdAt' timestamp"

    def test_crear_y_eliminar_usuario(self):
        """
        POST + DELETE - Flujo de crear y eliminar un recurso.
        
        Verifica encadenamiento de peticiones:
        1. Crear usuario (POST)
        2. Eliminar usuario (DELETE)
        """
        # Paso 1: Crear usuario
        payload = {"name": "neo", "job": "the one"}
        
        create_response = requests.post(
            f"{BASE_URL}/users",
            json=payload,
            headers=HEADERS
        )
        
        assert create_response.status_code == 201
        user_id = create_response.json().get("id")
        assert user_id is not None, "Created user should have an ID"
        
        # Paso 2: Eliminar usuario (ReqRes simula la eliminación)
        delete_response = requests.delete(
            f"{BASE_URL}/users/{user_id}",
            headers=HEADERS
        )
        
        # DELETE exitoso devuelve 204 No Content
        assert delete_response.status_code == 204, \
            f"Expected 204, got {delete_response.status_code}"

    def test_usuario_no_encontrado(self):
        """
        GET /users/{id} - Usuario que no existe.
        
        Verifica:
        - Status code 404 (Not Found)
        - Respuesta vacía o con mensaje de error
        """
        response = requests.get(
            f"{BASE_URL}/users/9999",
            headers=HEADERS
        )
        
        assert response.status_code == 404, \
            f"Expected 404 for non-existent user, got {response.status_code}"

    def test_login_exitoso(self):
        """
        POST /login - Login simulado exitoso.
        
        Verifica:
        - Status code 200
        - Respuesta contiene token
        """
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        
        response = requests.post(
            f"{BASE_URL}/login",
            json=payload,
            headers=HEADERS
        )
        
        assert response.status_code == 200
        assert "token" in response.json()

    def test_login_fallido_sin_password(self):
        """
        POST /login - Login sin password (escenario negativo).
        
        Verifica:
        - Status code 400 (Bad Request)
        - Respuesta contiene mensaje de error
        """
        payload = {
            "email": "peter@klaven"
            # Sin password
        }
        
        response = requests.post(
            f"{BASE_URL}/login",
            json=payload,
            headers=HEADERS
        )
        
        assert response.status_code == 400
        assert "error" in response.json()