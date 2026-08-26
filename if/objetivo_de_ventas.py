import os 
def objetivo_de_ventas():
    os.system("cls")    
    """
    Tu misión: Un emprendimiento fija una meta diaria de C$4,000.
      Lee el total vendido e informa si se alcanzó; muestra cuánto faltó o 
      cuánto se superó.
      """
    print("-----Bienvenido a pulseras masayitas-----")
    print("Ingrese el total vendido del día:")
    total_vendido = float(input())
    meta_diaria = 4000.0
    if total_vendido >= meta_diaria:
        print(f"¡Felicidades! Se alcanzó la meta diaria de C${meta_diaria:.2f}.")
        print(f"Se superó la meta en C${total_vendido - meta_diaria:.2f}.")
    else:
        print(f"No se alcanzó la meta diaria de C${meta_diaria:.2f}.")
        print(f"Faltaron C${meta_diaria - total_vendido:.2f} para alcanzar la meta.")
if __name__ == "__main__":
  objetivo_de_ventas()
