import os

def combustible_de_reparto():
    os.system("cls")
    """
    Tu misión: Una motocicleta inicia con 8 litros. 
    Registra el consumo de cada recorrido mientras quede combustible 
    y alerta al llegar a 1 litro.
    """
    print("=== COMBUSTIBLE DE REPARTO ===")
    print()

    combustible = 8.0  # Litros iniciales
    recorrido = 0

    print(f"Combustible inicial: {combustible} litros\n")

    while combustible > 0:
        recorrido += 1
        print(f"--- Recorrido {recorrido} ---")
        print(f"Combustible disponible: {combustible:.1f} litros")
        
        try:
            consumo = float(input("Ingrese consumo de este recorrido (litros): "))
            
            if consumo <= 0:
                print("  ⚠️  Error: El consumo debe ser positivo\n")
                continue
            
            if consumo > combustible:
                print(f"  ⚠️  Error: No hay suficiente combustible. Máximo: {combustible:.1f} litros\n")
                continue
            
            combustible -= consumo
            
            if combustible < 1:
                print(f"  🔴 ALERTA: Combustible crítico: {combustible:.1f} litros")
            elif combustible == 0:
                print(f"  🔴 ALERTA: Sin combustible. Viaje finalizado.")
            
            print()
        except ValueError:
            print("  ⚠️  Error: Ingrese un número válido\n")

    print("--- RESUMEN DEL VIAJE ---")
    print(f"Total de recorridos: {recorrido}")
    print(f"Combustible restante: {combustible:.1f} litros")

if __name__ == "__main__":
    combustible_de_reparto()
