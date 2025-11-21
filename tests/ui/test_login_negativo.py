"""
Test de Login - Escenarios Negativos
====================================

Este módulo contiene casos de prueba negativos para la funcionalidad de login.
Verifica que el sistema maneje correctamente credenciales inválidas.
"""

import pytest
from pages.login_page import LoginPage


class TestLoginNegativo:
    """Casos de prueba negativos para el login de SauceDemo."""

    def test_login_usuario_invalido(self, browser):
        """
        Verifica que se muestre error al usar un usuario que no existe.
        
        Pasos:
        1. Navegar a la página de login
        2. Ingresar usuario inexistente y contraseña cualquiera
        3. Hacer clic en Login
        4. Verificar mensaje de error
        """
        login = LoginPage(browser)
        login.abrir()
        
        # Intentar login con usuario que no existe
        login.login("usuario_falso", "password123")
        
        error = login.obtener_mensaje_error()
        assert "Epic sadface" in error
        assert "Username and password do not match" in error

    def test_login_password_incorrecta(self, browser):
        """
        Verifica que se muestre error con usuario válido pero contraseña incorrecta.
        
        Pasos:
        1. Navegar a la página de login
        2. Ingresar usuario válido con contraseña incorrecta
        3. Hacer clic en Login
        4. Verificar mensaje de error
        """
        login = LoginPage(browser)
        login.abrir()
        
        # Usuario válido, contraseña incorrecta
        login.login("standard_user", "contraseña_incorrecta")
        
        error = login.obtener_mensaje_error()
        assert "Epic sadface" in error

    def test_login_campos_vacios(self, browser):
        """
        Verifica que se muestre error al intentar login sin credenciales.
        
        Pasos:
        1. Navegar a la página de login
        2. Dejar campos vacíos
        3. Hacer clic en Login
        4. Verificar mensaje de error
        """
        login = LoginPage(browser)
        login.abrir()
        
        # Intentar login sin ingresar nada
        login.login("", "")
        
        error = login.obtener_mensaje_error()
        assert "Username is required" in error

    def test_login_solo_usuario(self, browser):
        """
        Verifica que se muestre error al ingresar solo el usuario.
        
        Pasos:
        1. Navegar a la página de login
        2. Ingresar solo usuario, dejar password vacío
        3. Hacer clic en Login
        4. Verificar mensaje de error
        """
        login = LoginPage(browser)
        login.abrir()
        
        login.login("standard_user", "")
        
        error = login.obtener_mensaje_error()
        assert "Password is required" in error

    def test_login_usuario_bloqueado(self, browser):
        """
        Verifica el mensaje de error para usuario bloqueado.
        
        Pasos:
        1. Navegar a la página de login
        2. Ingresar credenciales del usuario bloqueado
        3. Verificar mensaje específico de bloqueo
        """
        login = LoginPage(browser)
        login.abrir()
        
        # Usuario bloqueado de SauceDemo
        login.login("locked_out_user", "secret_sauce")
        
        error = login.obtener_mensaje_error()
        assert "locked out" in error.lower()