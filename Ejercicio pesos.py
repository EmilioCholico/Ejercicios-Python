import math
print("¿Qué moneda deseas convertir? \na)Pesos a dolares\nb)Dolares a pesos \nConversión deseada:")
moneda = input()
print("Ingresa el monto:")
cantidad = float(input())
if moneda == 'a':
    resultado = math.ceil((cantidad / 18.20)*100)/100
    print(resultado, "dolares")
elif moneda == 'b':
    resultado = math.ceil((cantidad * 18.20)*100)/100
    print(resultado, "pesos")
else:
    print("Moneda no valida")
