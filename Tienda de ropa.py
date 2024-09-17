from os import system
salir = False

while not salir:
    try:
        print("\nBienvenido estimado colaborador, recuerda atender correctamente a nuestros clientes\n")
        while True:
            cuenta = input("Tipo de cuenta del cliente (Normal o VIP): ").lower()
            if cuenta in ['normal', 'vip']:
                try:
                    monto = float(input("\nMonto a cobrar: $"))
                    if cuenta == 'vip':
                        desvip = (monto / 100) * 5
                        print(f"Por ser cliente VIP con nosotros se le ha generado un descuento de: $",desvip)
                    break
                except ValueError:
                    print("Por favor, ingrese un monto válido (números).")
            else:
                print("Favor de ingresar Normal o VIP.")
    except ValueError:
                print("Favor de ingresar Normal o VIP")
    else:
        if monto >= 1000:
            des = (monto / 100)*10
            if cuenta.lower() == 'vip':
                pago = (monto - desvip - des)
                print("\nUsted está ahorrando además: " , "\n$" , des , "\nPor su compra mayor a $1000 pesos")
                print("\nSu pago a realizar es de:" ,"\n$" ,pago)
            else:
                pagot = (monto - des)
                print("\nSu pago a realizar es de:" ,"\n$", pagot)
                print("\nUsted está ahorrando:" , "\n$" , des , "\nPor su compra mayor a $1000 pesos")
        elif monto >= 500 and monto <1000:
            descu = (monto / 100)*5
            if cuenta.lower() == 'vip':
                pagoto = (monto - desvip - descu)
                print("\nSu pago a realizar es de:" , "\n$" , pagoto)
                print("\nUsted está ahorrando:" , "\n$" , descu , "\nPor su compra mayor a $500 pesos ")
            else:
                pagototals = (monto - descu)
                print("\nSu pago a realizar es de:" , "\n$" , pagototals)
                print("\nUsted está ahorrando:" , "\n$" , descu , "\nPor su compra mayor a $500 pesos")
        elif monto < 500:
            if cuenta.lower() == 'vip':
                pagotota = (monto - desvip)
                print("\nSu pago a realizar es de:" , "\n$" , pagotota)
                print("\nUsted está ahorrando:" , "\n$" , desvip)
            else:
                pagototal = monto
                print("\nSu pago total es de:" , "\n$" , monto , "\n¡Agradecemos su visita!")
        else:
            print("Favor de ingresar un monto correcto")
    finally:
        continuar = ''
        while continuar.lower() not in ['si','no']:
                continuar = input("\nDesea realizar otra venta (si/no):")
                salir = True if continuar.lower() == 'no' else False
                system("cls")
