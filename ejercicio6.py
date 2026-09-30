#ejercicio 6

letra = input("ingrese una letra: ")
if len(letra) != 1:
    print("ingrese solo una letra")
else:
    letra = letra.lower()
    if letra in ['a', 'e', 'i', 'o', 'u']:
        print("es una vocal")
    else:
        print("es una consonante")