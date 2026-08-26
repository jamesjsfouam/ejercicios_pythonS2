import os 
def promocion():
    os.system("cls")    
    """
    Una tienda de Masaya aplica una promoción simulada de 10% cuando la compra supera C$1,500.
      Solicita el monto y muestra el total.
      """
    print("Bienvenido a la tienda de Masaya")
    producto = input("Ingrese el nombre de su producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad de productos: "))
    monto = precio * cantidad
    if monto > 1500:
        descuento = monto * 0.10
        total = monto - descuento
        print ("----Factura----:")
        print (f"Producto: {producto}")
        print(f"El monto de su compra es: C${monto:.2f}")
        print(f"Se aplicó un descuento del 10%: C${descuento:.2f}")
        print(f"El total a pagar es: C${total:.2f}")
    else:
        print ("----Factura----:")
        print (f"Producto: {producto}")
        print(f"El monto de su compra es: C${monto:.2f}")
        print("No se aplicó ningún descuento.")
if __name__ == "__main__":
  promocion()