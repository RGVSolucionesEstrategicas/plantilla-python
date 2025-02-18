# Plantilla RGV Python

Este repositorio sirve como plantilla para ejecutar scripts en Python 3.13 con soporte para variables de entorno y gestión de dependencias.

## Configuración

### 1. Crear y activar un entorno virtual

**Windows:**

```bash
py -3.13 -m venv venv
venv\Scripts\activate
```

**Linux y macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Renombrar `.env.example` a `.env` y modificar según sea necesario.

Ejemplo de `.env`:

```ini
USER_NAME=usuario_predeterminado
```

### 4. Ejecutar el script de prueba

```bash
python script.py
```

## FAQ

### ¿Qué es un entorno virtual?

Un entorno virtual es un entorno aislado en el que se pueden instalar dependencias sin afectar al sistema global. Permite gestionar diferentes versiones de paquetes para distintos proyectos.

### ¿Qué son las dependencias?

Las dependencias son paquetes externos que un proyecto necesita para funcionar. Se gestionan con `pip` y se listan en `requirements.txt`.

**Comandos básicos para manejar dependencias:**

- Instalar dependencias desde `requirements.txt`:

  ```bash
  pip install -r requirements.txt
  ```

- Agregar una nueva dependencia y actualizar `requirements.txt`:

  ```bash
  pip install nombre_paquete
  pip freeze > requirements.txt
  ```

### ¿Qué son las variables de entorno?

Las variables de entorno son configuraciones externas que se pueden usar en un script sin necesidad de estar embebidas en el código. Permiten mayor flexibilidad y seguridad.
