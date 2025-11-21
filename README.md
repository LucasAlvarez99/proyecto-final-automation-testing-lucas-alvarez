# 🧪 Framework de Automatización de Pruebas

**Proyecto Final - Automation Testing**  
**Alumno:** Lucas Alvarez  
**Curso:** Testing QA - Automatización

---

## 📋 Propósito del Proyecto

Este framework de automatización de pruebas está diseñado para validar la funcionalidad de aplicaciones web y APIs REST. Combina pruebas de interfaz de usuario (UI) utilizando Selenium WebDriver con pruebas de API utilizando la biblioteca Requests.

### Objetivos principales:
- Automatizar flujos críticos de usuario (login, navegación, carrito, checkout)
- Validar endpoints de APIs REST (GET, POST, DELETE)
- Generar reportes HTML detallados con evidencias
- Implementar el patrón Page Object Model para código mantenible
- Capturar screenshots automáticamente en caso de fallos

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.8+ | Lenguaje principal |
| Pytest | ≥7.0 | Framework de testing |
| Selenium WebDriver | ≥4.10 | Automatización de UI |
| Requests | ≥2.31 | Pruebas de API |
| pytest-html | ≥3.2 | Generación de reportes HTML |
| webdriver-manager | ≥4.0 | Gestión automática de drivers |

---

## 📁 Estructura del Proyecto

```
proyecto-final-automation-testing-lucas-alvarez/
│
├── 📂 datos/                    # Datos de prueba externos
│   └── user.csv                 # Credenciales para login parametrizado
│
├── 📂 logs/                     # Logs de ejecución (generado automático)
│   └── test_name_YYYY-MM-DD.log
│
├── 📂 pages/                    # Page Object Model - Clases de páginas
│   ├── __init__.py
│   ├── base_page.py             # Clase base con métodos comunes
│   ├── login_page.py            # Página de login
│   ├── inventory_page.py        # Página de inventario/productos
│   ├── cart_page.py             # Página del carrito
│   ├── checkout_step_one_page.py    # Checkout paso 1
│   ├── checkout_step_two_page.py    # Checkout paso 2
│   └── checkout_complete_page.py    # Checkout completado
│
├── 📂 reports/                  # Reportes HTML (generado automático)
│   └── reporte.html
│
├── 📂 screenshots/              # Capturas de pantalla en fallos
│   └── test_name_YYYY-MM-DD.png
│
├── 📂 tests/                    # Casos de prueba
│   ├── 📂 api/                  # Pruebas de API
│   │   └── test_api_reqres.py   # Tests contra ReqRes API
│   │
│   └── 📂 ui/                   # Pruebas de interfaz
│       ├── test_login.py        # Test de login básico
│       ├── test_login_parametrizado.py  # Login con múltiples datos
│       ├── test_cart.py         # Test de carrito
│       └── test_checkout.py     # Test de checkout completo
│
├── 📂 utils/                    # Utilidades y helpers
│   ├── __init__.py
│   ├── data_reader.py           # Lectura de archivos CSV/JSON
│   ├── helpers.py               # Funciones auxiliares (waits, screenshots)
│   └── logger.py                # Sistema de logging
│
├── conftest.py                  # Fixtures de pytest
├── pytest.ini                   # Configuración de pytest
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Este archivo
```

---

## ⚙️ Instalación

### Prerrequisitos
- Python 3.8 o superior
- Google Chrome instalado
- Git

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/proyecto-final-automation-testing-lucas-alvarez.git
cd proyecto-final-automation-testing-lucas-alvarez
```

2. **Crear y activar entorno virtual**
```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Linux/macOS
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución de Pruebas

### Ejecutar todas las pruebas
```bash
pytest
```

### Ejecutar con reporte HTML detallado
```bash
pytest --html=reports/reporte.html --self-contained-html
```

### Ejecutar solo pruebas de UI
```bash
pytest tests/ui/ -v
```

### Ejecutar solo pruebas de API
```bash
pytest tests/api/ -v
```

### Ejecutar un test específico
```bash
pytest tests/ui/test_login.py -v
```

### Ejecutar con más detalle (verbose)
```bash
pytest -v --tb=short
```

### Ejecutar en modo headless (sin interfaz gráfica)
Descomentar la línea en `conftest.py`:
```python
chrome_options.add_argument("--headless")
```

---

## 📊 Interpretación de Reportes

### Reporte HTML (`reports/reporte.html`)

Después de ejecutar las pruebas, abrir el archivo `reports/reporte.html` en un navegador.

**Secciones del reporte:**
- **Summary**: Resumen general con cantidad de tests pasados/fallidos
- **Environment**: Información del entorno (Python, SO, plugins)
- **Results Table**: Detalle de cada test ejecutado

**Estados posibles:**
| Estado | Significado |
|--------|-------------|
| ✅ Passed | La prueba pasó correctamente |
| ❌ Failed | La prueba falló (ver detalles y screenshot) |
| ⏭️ Skipped | La prueba fue omitida |
| ⚠️ Error | Error en la configuración/fixture |

### Logs (`logs/`)

Cada ejecución genera un archivo de log con:
- Timestamp de cada acción
- Pasos ejecutados
- Errores encontrados
- Rutas de screenshots capturados

### Screenshots (`screenshots/`)

Las capturas se generan automáticamente cuando una prueba falla. El nombre incluye:
- Nombre del test
- Fecha y hora de la captura

---

## 🧪 Casos de Prueba Implementados

### Pruebas de UI (Selenium) - SauceDemo

| Test | Descripción | Tipo |
|------|-------------|------|
| `test_login_exitoso` | Login con credenciales válidas | Positivo |
| `test_login_parametrizado` | Login con múltiples usuarios (CSV) | Parametrizado |
| `test_agregar_producto_al_carrito` | Agregar producto y verificar carrito | Positivo |
| `test_checkout_completo` | Flujo completo de compra | E2E |

### Pruebas de API (Requests) - ReqRes

| Test | Método | Descripción |
|------|--------|-------------|
| `test_get_users` | GET | Obtener lista de usuarios |
| `test_create_user_and_delete` | POST + DELETE | Crear y eliminar usuario |
| `test_get_single_user_not_found` | GET | Validar 404 para usuario inexistente |

---

## 📝 Datos de Prueba

### Archivo: `datos/user.csv`
```csv
username,password,resultado
standard_user,secret_sauce,ok
locked_out_user,secret_sauce,error
problem_user,secret_sauce,ok
fake_user,123,error
```

---

## 🏗️ Patrón Page Object Model

El proyecto implementa POM para separar la lógica de las pruebas de la interacción con la UI:

```
BasePage (clase base)
    ├── navegar(url)
    ├── encontrar(locator)
    ├── click(locator)
    ├── escribir(locator, texto)
    └── obtener_texto(locator)

LoginPage → InventoryPage → CartPage → CheckoutPages
```

**Ventajas:**
- Código reutilizable y mantenible
- Cambios en la UI requieren modificar solo una clase
- Tests más legibles y enfocados en el comportamiento

---

## 🔧 Configuración Adicional

### pytest.ini
```ini
[pytest]
minversion = 6.0
addopts = -ra -q --html=reports/reporte.html --self-contained-html
testpaths = tests
```

### Variables de entorno (opcional)
Crear archivo `.env` para configuraciones sensibles:
```
BASE_URL=https://www.saucedemo.com
API_URL=https://reqres.in/api
```

---

## 📈 Mejoras Futuras

- [ ] Integración con GitHub Actions (CI/CD)
- [ ] Pruebas de rendimiento con Locust
- [ ] Pruebas de accesibilidad
- [ ] Ejecución paralela de tests
- [ ] Integración con Allure Reports

---

## 👤 Autor

**Lucas Alvarez**  
Proyecto Final - Curso de Automation Testing

---

## 📄 Licencia

Este proyecto es de uso educativo.