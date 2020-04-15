sw = True

def suma(a, b):
    c = a + b
    return c
def resta(a, b):
    c = a - b
    return c
def multiplicacion(a, b):
    c = a * b
    return c
def division(a, b):
    c = a / b
    return c
def terminar_programa():
    print('Calculadora Cerrada')
    global sw
    sw = False
def opcion_no_disponible():
    print('Opcion no disponible')

menu = '''
*********CALCULADORA*********
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir de la Calculadora
'''
while sw:
    print(menu)
    opcion = int(input('Ingrese una opcion a realizar: '))

    if opcion == 1:
        uno = float(input('Ingrese el primer numero: '))
        dos = float(input('Ingrese el segundo numero: '))
        elige_suma = suma(uno, dos)
        print('La suma de los dos numeros es: ', elige_suma)
    elif opcion == 2:
        uno = float(input('Ingrese el primer numero: '))
        dos = float(input('Ingrese el segundo numero: '))
        elige_resta = resta(uno, dos)
        print('La resta de los dos numeros es: ', elige_resta)
    elif opcion == 3:
        uno = float(input('Ingrese el primer numero: '))
        dos = float(input('Ingrese el segundo numero: '))
        elige_multiplicacion = multiplicacion(uno, dos)
        print('La multiplicacion de los dos numeros es: ', elige_multiplicacion)
    elif opcion == 4:
        uno = float(input('Ingrese el primer numero: '))
        dos = float(input('Ingrese el segundo numero: '))
        elige_division = division(uno, dos)
        print('La suma de los dos numeros es: ', elige_division)
    elif opcion == 5:
        terminar_programa()
    else:
        opcion_no_disponible()