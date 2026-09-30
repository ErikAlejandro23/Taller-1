#ejercicio 7 el fizz buzz

numero = int(input("ingrese un numero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("fizz buzz")
elif numero % 3 == 0:
    print("fizz")
elif numero % 5 == 0:
    print("buzz")
else:
    print(numero)
