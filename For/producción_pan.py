import os

def producción_pan():
    os.system("cls")
    """
    Tu misión: Una panadería registra durante 6 días 
    la producción y las ventas. Calcula totales y producto sobrante.
    """
    print("=== REGISTRO DE PRODUCCIÓN Y VENTAS ===")
    print()

    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    total_produccion = 0
    total_ventas = 0

    for dia in dias:
        print(f"--- {dia} ---")
        produccion = int(input(f"  Panes producidos: "))
        ventas = int(input(f"  Panes vendidos: "))
        
        total_produccion += produccion
        total_ventas += ventas
        print()

    sobrante = total_produccion - total_ventas

    print("--- RESUMEN SEMANAL ---")
    print(f"Total producido: {total_produccion} panes")
    print(f"Total vendido: {total_ventas} panes")
    print(f"Producto sobrante: {sobrante} panes")

if __name__ == "__main__":
    producción_pan()
