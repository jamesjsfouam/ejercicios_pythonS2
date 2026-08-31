from ventas_minisúper import ventas_minisúper
from recepción_café import recepción_café
from revisión_inventario import revisión_inventario
from producción_pan import producción_pan
from evaluación_servicio import evaluación_servicio

def main():
    while True:
        print("\n ###  Catálogo de funciones - EJERCICIOS FOR ###")
        print("1.----- Ventas de un minisúper -----")
        print("2.----- Recepción de café -----")
        print("3.----- Revisión de inventario -----")
        print("4.----- Producción de pan -----")
        print("5.----- Evaluación del servicio -----")
        print("6.-----       Salir         -----")
        opcion = int(input("Ingrese el número de la opción deseada: "))

        match opcion:
            case 1:
                ventas_minisúper()
            case 2:
                recepción_café()
            case 3:
                revisión_inventario()
            case 4:
                producción_pan()
            case 5:
                evaluación_servicio()
            case 6:
                print("Saliendo del programa...")
                return
            case _:
                print("Opción no válida.")

        if opcion != 6:
            input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    main()
