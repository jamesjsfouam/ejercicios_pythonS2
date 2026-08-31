import os

def acceso_al_sistema():
    os.system("cls")
    """
    Tu misión: Solicita la clave hasta que sea correcta. 
    Cuenta los intentos e informa cuántos fueron necesarios.
    """
    print("=== ACCESO AL SISTEMA ===")
    print()

    clave_correcta = "python2024"
    intentos = 0

    while True:
        clave = input("Ingrese la clave de acceso: ")
        intentos += 1
        
        if clave == clave_correcta:
            print(f"\n✓ ¡Acceso concedido!")
            print(f"Número de intentos: {intentos}")
            break
        else:
            print(f"  ⚠️  Clave incorrecta. Intento {intentos}")
            print()

if __name__ == "__main__":
    acceso_al_sistema()
