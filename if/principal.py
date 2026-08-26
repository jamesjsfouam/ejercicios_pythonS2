from promocion import promocion
from Pulperia import pulperia
from entrega_comedor import entrega_comedor
from objetivo_de_ventas import objetivo_de_ventas
from peso_productos import peso_productos
def main():
    while True:
        print("\nBienvenido al programa de ejercicios de IF")
        print("1. Promoción de tienda")
        print("2. Pulpería La Esquina")
        print("3. Entrega de comedor")
        print("4. Objetivo de ventas")
        print("5. Peso de un producto")
        print("6. Salir")
        opcion = int(input("Ingrese el número de la opción deseada: "))

        match opcion:
            case 1:
                promocion()
            case 2:
                pulperia()
            case 3:
                entrega_comedor()
            case 4:
                objetivo_de_ventas()
            case 5:
                peso_productos()
            case 6:
                print("Saliendo del programa...")
                return
            case _:
                print("Opción no válida.")

        if opcion != 6:
            input("\nPresione Enter para volver al menú...")

main()