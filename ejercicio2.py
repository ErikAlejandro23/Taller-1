#SEGUNDO EJERCICIO 
print("Ingrese dos números y te dire le dirá cuál es el menor.")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 < numero2:
    print(f"El numero menor es: {numero1}")
elif numero2 < numero1:
    print(f"El numero menor es: {numero2}")
else:
    print("Los dos números son iguales")