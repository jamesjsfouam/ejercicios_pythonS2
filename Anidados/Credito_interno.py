import os
def credito_interno():
    """
    Una pulpería vende al crédito solo a clientes registrados. 
    Si lo están, revisa que su saldo pendiente no supere C$500.
      Diseña los mensajes para todos los casos.
      """
    print("----Bienvenido al sistema de prestamos doña juanita----")
    clientes_registrados = ("Armando","James","Jose","Gabriel")
    saldo_james = 200
    saldo_armando = 600
    saldo_jose = 499
    saldo_Gabriel = 20
    print("ingrese su nombre")
    cliente = input().strip().title()
    if cliente in clientes_registrados:
        print("Excelente, usted se encuentra registrado")
        saldos = {
            "Armando": saldo_armando,
            "James": saldo_james,
            "Jose": saldo_jose,
            "Gabriel": saldo_Gabriel,
        }
        print(f"su saldo pendiente es de {saldos.get(cliente, 0)}")
        if saldos.get(cliente, 0) <= 500:
            print("Usted puede acceder al crédito.")
        else:
            print("Lo siento, su saldo pendiente supera C$500.")
    else:
        print("Usted no está registrado en el sistema.")
credito_interno()
