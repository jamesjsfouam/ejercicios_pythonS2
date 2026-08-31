import os

def cierre_de_caja():
    os.system("cls")
    """
    Tu misión: Ingresa los montos de ventas hasta escribir 0. 
    Calcula el total recaudado y la cantidad de ventas.
    """
    print("=== CIERRE DE CAJA ===")
    print()

    total_recaudado = 0
    cantidad_ventas = 0

    while True:
        monto = float(input("Ingrese monto de venta (0 para terminar): C$"))
        
        if monto == 0:
            break
        
        if monto > 0:
            total_recaudado += monto
            cantidad_ventas += 1
            print(f"  ✓ Venta registrada")
        else:
            print("  ⚠️  Error: El monto debe ser positivo")
        
        print()

    print("--- RESUMEN DE CIERRE ---")
    print(f"Total recaudado: C${total_recaudado:.2f}")
    print(f"Cantidad de ventas: {cantidad_ventas}")

if __name__ == "__main__":
    cierre_de_caja()
