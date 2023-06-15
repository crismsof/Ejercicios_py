# Cristina Monterroso
# Función devolverNumero: Recibe un intervalo (límite inferior y superior) y
# devuelve el número intermedio como posible número que tiene que acertar.
# Parámetro de entrada: Límite inferior y superior del intervalo.
# Dato devuelto: Número intermedio del intervalo.


def devolverNumero(liminf, limsup):
    return (liminf + limsup) // 2  # 1,3 2 2,3 2, 2, 2, 2


# Función LeerOpcion: Recibe un intervalo (límite inferior y superior) y el número
# que ha propuesto como solución y devuelve la opción escogida:
# 'S', si es correcto.
# 'A', si es más alto que el número a adivinar.
# 'B', si es más bajo. Al finalizar el programa, se deberá escribir el número de
# intentos realizados para acertar el número.
# Si la opción es A, se modifica el límite inferior con el número propuesto.
# Si la opción es B, se modifica el límite superior con el número propuesto.
# Parámetro de entrada: Número propuesto
# Dato devuelto: Opción escogida, límite inferior y superior


def LeerOpcion(num, liminf, limsup):
    while True:
        print("¿Es correcto?")
        print(f"S: Sí, {num} es correcto!")
        print(f"A: No, el número a acertar es más alto que {num}.")
        print(f"B: No, el número a acertar es más bajo que {num}.")
        opcion = input()
        if opcion.upper() == "S" or opcion.upper() == "A" or opcion.upper() == "B":
            break
    if opcion.upper() == "A":  # 0-23 -> 22-23
        return opcion, num, limsup
    if opcion.upper() == "B":
        return opcion, liminf, num
    return opcion, liminf, limsup


# Diseñar un programa que permita adivinar al ordenador un determinado número
# entero y positivo para lo cual se deben leer los límites en los que está
# comprendido dicho número.


def validar_input_int(texto_input):
    while True:
        try:
            valor = int(input(texto_input))
            return valor
        except:
            print("Error, se esperaba número entero.")


intentos = 0
print("Piensa un número...")
# Se pide el primer intervalo
print("Necesito saber el intervalo donde se encuentra el número:")

limite_inferior = validar_input_int("Límite inferior:")
while True:
    limite_superior = validar_input_int("Límite superior:")
    if limite_inferior < limite_superior:
        break
    else:
        print(
            "Error, el límite superior ha de tener un valor mayor al límite inferior."
        )

# Se va repitiendo hasta que se acierte el número
minumero = 0
while True:
    # Escribimos el número propuesto (qué sera el número intermedio del intervalo)
    minumeroanterior = minumero
    minumero = devolverNumero(limite_inferior, limite_superior)
    if minumeroanterior == minumero:
        minumero += 1
    print(f"¿Has pensando en el número {minumero}?")
    # Incrementamos el número de intentos
    intentos = intentos + 1
    # Leemos la opción, si no ha acertado se modifica algunos de los límites y se vuelve a proponer un nuevo número
    opcion, limite_inferior, limite_superior = LeerOpcion(
        minumero, limite_inferior, limite_superior
    )
    if opcion.upper() == "S":
        break
# Se escribe los intentos que ha necesitado para acertarlo
print("Lo he acertado en", intentos, "intentos.")

# >-----------
# Validamos input integer de los valores límite a través de funcion general, validamos que el valor del límite superior es mayor al límite inferior, corregimos error decimal al buscar entre limites no mayores de 1 entre ellos, aclaramos las opciones al presentar el menu del restultado
# >-----------
