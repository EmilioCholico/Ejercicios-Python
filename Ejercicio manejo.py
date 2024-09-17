from os import system
salir = False

while not salir:
    try:
        print("\nBienvenido al sistema para validar conducción" +
        "\nFavor de ingresar los siguientes datos:")
        edad = int(input("\nIndicar la edad actual de la persona:"))
        lic = input("\nIndicar si tiene o no licencia(si/no):")
    except ValueError:
        print("\nFavor de ingresar un número entero\n")
    else:
        if edad >= 18 and lic == 'si':
            print("\n**La persona es apta para conducir**\n")
            
        elif edad < 18 or lic == "no":
            print("\n**Que ni toque el coche por que lo multamos y pal tambo**\n")
        else:
            print("\nFavor de ingresar si o no\n")
    finally:
        terminar = ''
        while terminar.lower() not in ['si','no']:
            terminar = input("Desea verificar algúna otra persona (si/no):")
            salir = True if terminar.lower() == 'no' else False
            system("cls")
