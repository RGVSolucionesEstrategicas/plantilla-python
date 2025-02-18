import os
from dotenv import load_dotenv


def main():
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    # Leer variables de entorno
    user_name = os.getenv("USER_NAME", "Invitado")

    # Mostrar mensaje con la variable de entorno
    print(f"Hola, {user_name}! Bienvenido al script de prueba.")


if __name__ == "__main__":
    main()
