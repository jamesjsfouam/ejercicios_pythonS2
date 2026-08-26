import os
def entrega_comedor():
    os.system("cls")
    """
    Entrega de un comedor.

    La entrega es gratuita desde C$300. En caso contrario,
    se suma un recargo de C$40.
    """
    print("-----Bienvenido a fritanga solimari-----")
    cantidad_pollo = int(input("¿Cuánto pollo asado desea llevar? (C$120 cada uno): "))
    cantidad_carne = int(input("¿Cuánta carne asada desea llevar? (C$150 cada una): "))

    precio_pollo = 120
    precio_carne = 150
    recargo_entrega = 40

    subtotal_pollo = cantidad_pollo * precio_pollo
    subtotal_carne = cantidad_carne * precio_carne
    subtotal = subtotal_pollo + subtotal_carne

    entrega_gratis = subtotal >= 300

    if entrega_gratis:
        costo_entrega = 0
    else:
        costo_entrega = recargo_entrega

    total = subtotal + costo_entrega

    print("\n----------- RECIBO -----------")
    print(f"Pollo asado: {cantidad_pollo} x C${precio_pollo} = C${subtotal_pollo}")
    print(f"Carne asada: {cantidad_carne} x C${precio_carne} = C${subtotal_carne}")
    print(f"Subtotal: C${subtotal}")

    if entrega_gratis:
        print("Entrega: Gratis")
    else:
        print(f"Entrega: C${costo_entrega}")

    print(f"TOTAL A PAGAR: C${total}")


if __name__ == "__main__":
    entrega_comedor()
        
