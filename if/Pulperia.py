# La pulperia La Esquina necesita reponer un producto cuando quedan menos de 5 unidades.
import os 
def pulperia():
    os.system("cls")
    nombre = input("Ingrese el nombre del producto: ")
    existencia = int(input("Ingrese la cantidad disponible: "))
    precio = float(input("Ingrese el precio del producto: "))

    print(f"\nProducto: {nombre}")
    print(f"Existencia: {existencia} unidades")
    print(f"Precio: C${precio:.2f}")

    if existencia < 5:
        print(f"Alerta: debe reponer {nombre}.")
    else:
        print("La existencia del producto es suficiente.")