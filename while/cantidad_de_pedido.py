import os

def cantidad_de_pedido():
    os.system("cls")
    """
    Tu misión: Un distribuidor acepta de 1 a 100 unidades. 
    Solicita la cantidad hasta que sea válida y luego calcula el total.
    """
    print("=== CANTIDAD DE UN PEDIDO ===")
    print()

    precio_unitario = 50  # Precio en córdobas

    while True:
        try:
            cantidad = int(input("Ingrese cantidad de unidades (1-100): "))
            
            if 1 <= cantidad <= 100:
                print(f"  ✓ Cantidad válida: {cantidad} unidades")
                break
            else:
                print(f"  ⚠️  Error: Debe ser entre 1 y 100 unidades\n")
        except ValueError:
            print("  ⚠️  Error: Ingrese un número entero\n")

    total = cantidad * precio_unitario

    print(f"\n--- RESUMEN DEL PEDIDO ---")
    print(f"Cantidad: {cantidad} unidades")
    print(f"Precio unitario: C${precio_unitario:.2f}")
    print(f"Total: C${total:.2f}")

if __name__ == "__main__":
    cantidad_de_pedido()
