from cierre_de_caja import cierre_de_caja
from acceso_al_sistema import acceso_al_sistema
from cantidad_de_pedido import cantidad_de_pedido
from combustible_de_reparto import combustible_de_reparto
from reposicion_de_existencias import reposicion_de_existencias

def main():
    while True:
        print("\n ###  Catálogo de funciones - EJERCICIOS WHILE ###")
        print("1.----- Cierre de caja -----")
        print("2.----- Acceso al sistema -----")
        print("3.----- Cantidad de un pedido -----")
        print("4.----- Combustible de reparto -----")
        print("5.----- Reposición de existencias -----")
        print("6.-----       Salir         -----")
        opcion = int(input("Ingrese el número de la opción deseada: "))

        match opcion:
            case 1:
                cierre_de_caja()
            case 2:
                acceso_al_sistema()
            case 3:
                cantidad_de_pedido()
            case 4:
                combustible_de_reparto()
            case 5:
                reposicion_de_existencias()
            case 6:
                print("Saliendo del programa...")
                return
            case _:
                print("Opción no válida.")

        if opcion != 6:
            input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    main()
