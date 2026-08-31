import os

def reposicion_de_existencias():
    os.system("cls")
    """
    Tu misión: Una tienda tiene 3 unidades y desea llegar a 20. 
    Solicita cada reposición y termina al alcanzar o superar la meta.
    """
    print("=== REPOSICIÓN DE EXISTENCIAS ===")
    print()

    existencia = 3
    meta = 20
    reposiciones = 0

    print(f"Existencia actual: {existencia} unidades")
    print(f"Meta: {meta} unidades\n")

    while existencia < meta:
        reposiciones += 1
        print(f"--- Reposición {reposiciones} ---")
        print(f"Existencia: {existencia} unidades")
        print(f"Falta: {meta - existencia} unidades")
        
        try:
            cantidad = int(input("¿Cuántas unidades reponer?: "))
            
            if cantidad <= 0:
                print("  ⚠️  Error: Debe reponer una cantidad positiva\n")
                continue
            
            existencia += cantidad
            print(f"  ✓ Nueva existencia: {existencia} unidades")
            
            if existencia >= meta:
                print(f"  ✓ ¡Meta alcanzada!")
            
            print()
        except ValueError:
            print("  ⚠️  Error: Ingrese un número entero\n")

    print("--- RESUMEN DE REPOSICIÓN ---")
    print(f"Existencia final: {existencia} unidades")
    print(f"Total de reposiciones: {reposiciones}")
    print(f"Excedente sobre la meta: {existencia - meta} unidades")

if __name__ == "__main__":
    reposicion_de_existencias()
