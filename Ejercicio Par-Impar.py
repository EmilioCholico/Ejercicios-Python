def main():
    print("Ingresa un numero (Ojo solo numeros enteros):")

    n = int(input())

    if n % 2 == 0:
        print(n, "es un número par\n")
        return main()
    elif n % 2 == 1:
        print(n, "es un número impar\n")
        return main()
    else:
        print("Favor de ingresar un dato correcto\n")
        return


main()
