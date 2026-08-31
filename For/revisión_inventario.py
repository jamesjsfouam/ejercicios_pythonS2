import os

def revisión_inventario():
    os.system("cls")
    """
    Tu misión: Una distribuidora revisa 8 productos. 
    Solicita nombre y existencia; muestra los que tienen menos de 10 unidades 
    y cuenta las alertas.
    """
    print("=== REVISIÓN DE INVENTARIO ===")
    print()

    productos_alerta = 0
    numero_productos = 8

    for producto in range(1, numero_productos + 1):
        nombre = input(f"Nombre del producto {producto}: ")
        existencia = int(input(f"  Existencia en stock: "))
        
        if existencia < 10:
            print(f"  ⚠️  ALERTA: Bajo stock en '{nombre}' ({existencia} unidades)\n")
            productos_alerta += 1
        else:
            print(f"  ✓ '{nombre}' en stock normal ({existencia} unidades)\n")

    print("--- RESUMEN ---")
    print(f"Total de productos revisados: {numero_productos}")
    print(f"Productos con alerta: {productos_alerta}")

if __name__ == "__main__":
    revisión_inventario()
