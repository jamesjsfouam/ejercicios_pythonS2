import os

def evaluación_servicio():
    os.system("cls")
    """
    Tu misión: Un restaurante recoge 10 calificaciones entre 1 y 5. 
    Calcula el promedio y cuenta cuántas fueron 4 o 5.
    """
    print("=== EVALUACIÓN DEL SERVICIO ===")
    print()
    print("Escala: 1 (Muy malo) a 5 (Excelente)\n")

    total_calificaciones = 0
    calificaciones_altas = 0
    numero_clientes = 10

    for cliente in range(1, numero_clientes + 1):
        calificacion = int(input(f"Calificación del cliente {cliente}: "))
        
        # Validar que esté en rango
        while calificacion < 1 or calificacion > 5:
            print("  Error: La calificación debe estar entre 1 y 5")
            calificacion = int(input(f"Calificación del cliente {cliente}: "))
        
        total_calificaciones += calificacion
        
        if calificacion >= 4:
            calificaciones_altas += 1

    promedio = total_calificaciones / numero_clientes

    print(f"\n--- RESULTADOS ---")
    print(f"Promedio de calificación: {promedio:.1f}/5.0")
    print(f"Clientes satisfechos (4-5): {calificaciones_altas} de {numero_clientes}")
    print(f"Porcentaje de satisfacción: {(calificaciones_altas/numero_clientes)*100:.1f}%")

if __name__ == "__main__":
    evaluación_servicio()
