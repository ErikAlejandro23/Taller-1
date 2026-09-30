#se pasa se roña con esta madre 
#instituto 

import re

def procesar_observaciones():
    # Pedir entrada al usuario
    entrada = input("Ingrese la fecha actual en formato 'día, DD/MM' (ej: martes, 15/05): ").strip()
    
    # Expresión regular para separar el día, el número de día y el número de mes
    patron = r"^([a-zA-ZáéíóúÁÉÍÓÚñÑ]+),\s*(\d{1,2})/(\d{1,2})$"
    coincidencia = re.match(patron, entrada)

    if not coincidencia:
        print("Error: El formato de entrada es incorrecto.")
        return

    dia_nombre = coincidencia.group(1).lower()
    # Eliminar tildes para uniformar la validación
    dia_nombre = dia_nombre.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
    
    dia = int(coincidencia.group(2))
    mes = int(coincidencia.group(3))

    dias_validos = ["lunes", "martes", "miercoles", "jueves", "viernes"]

    # Validación estricta según el enunciado
    if dia_nombre not in dias_validos or dia < 1 or dia > 31 or mes < 1 or mes > 12:
        print("Se produjo un error.")
        return

    # Lógica por nivel/día
    if dia_nombre in ["lunes", "martes", "miercoles"]:
        # Niveles Inicial, Intermedio y Avanzado
        hubo_examenes = input("¿Se tomaron exámenes hoy? (si/no): ").strip().lower()
        if hubo_examenes in ("si", "sí"):
            aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
            no_aprobados = int(input("Ingrese la cantidad de alumnos no aprobados: "))
            total = aprobados + no_aprobados
            if total > 0:
                porcentaje = (aprobados / total) * 100
                print(f"Porcentaje de aprobados: {porcentaje:.2f}%")
            else:
                print("No se ingresaron alumnos.")

    elif dia_nombre == "jueves":
        # Práctica Hablada
        asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
        if asistencia > 50:
            print("asistió la mayoría")
        else:
            print("no asistió la mayoría")

    elif dia_nombre == "viernes":
        # Inglés para Viajeros
        if dia == 1 and (mes == 1 or mes == 7):
            print("Comienzo de nuevo ciclo")
            cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel = float(input("Ingrese el arancel en $ por alumno: "))
            ingreso_total = cantidad_alumnos * arancel
            print(f"Ingreso total: ${ingreso_total:.2f}")

if __name__ == "__main__":
    procesar_observaciones()