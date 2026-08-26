import os 
def peso_productos():
    os.system("cls")    
    """
    Peso de productos
Tu misión: Una bodega espera sacos de 46 kg. 
Lee el peso e informa si cumple o debe revisarse por estar debajo del valor esperado.
    """
    print("----Bienvenido a bodega la esquinita----")
    peso = float(input("Ingrese el peso del saco en kg: "))
    peso_esperado = 46.0

    if peso < peso_esperado:
        print("El saco debe revisarse por estar debajo del valor esperado.")
    else:
        print("El saco cumple con el peso esperado.")
if __name__ == "__main__":
    peso_productos()