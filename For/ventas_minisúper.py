import os

def ventas_minisúper():
    os.system("cls")
    """
    Tu misión: Registra las ventas de lunes a domingo. 
    Calcula el total semanal y el promedio diario.
    """
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    total_semanal = 0

    print("=== REGISTRO DE VENTAS SEMANAL ===")
    print()

    for dia in dias:
        venta = float(input(f"Venta del {dia}: $"))
        total_semanal += venta

    promedio_diario = total_semanal / 7

    print(f"\n--- RESULTADOS ---")
    print(f"Total semanal: ${total_semanal:.2f}")
    print(f"Promedio diario: ${promedio_diario:.2f}")

if __name__ == "__main__":
    ventas_minisúper()
