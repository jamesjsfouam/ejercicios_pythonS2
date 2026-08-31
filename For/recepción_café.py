import os

def recepción_café():
    os.system("cls")
    """
    Tu misión: Una cooperativa recibe 5 sacos. 
    Solicita el peso de cada uno, muestra su número de recepción 
    y calcula el peso total.
    """
    print("=== RECEPCIÓN DE CAFÉ ===")
    print()

    total_peso = 0
    numero_sacos = 5

    for saco in range(1, numero_sacos + 1):
        peso = float(input(f"Peso del saco #{saco} (kg): "))
        print(f"  ✓ Saco #{saco} recibido: {peso} kg")
        total_peso += peso

    print(f"\n--- RESUMEN ---")
    print(f"Total de sacos recibidos: {numero_sacos}")
    print(f"Peso total: {total_peso} kg")

if __name__ == "__main__":
    recepción_café()
