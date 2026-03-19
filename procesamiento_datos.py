def suma(n,n1):
    return n + n1
def resta(n, n1):
    return n - n1
def multiplicacion(n, n1):
    return n * n1
def division(n, n1):
    if n1 != 0:
        return n / n1
    else:
        return " No es posible dividir por cero"

def mod(n, n1):
    if n1 != 0:
        return n % n1
    else:
        return " No es posible calcular el mod por cero"

def calculadora():
    while True:
        print("\nCalculadora Básica")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Mod")
        print("6. Salir")
        print("")
        opcion = int(input("Ingrese el número de la operación que desea realizar: "))
        print("")
        if opcion == 6:
            print("Ha salido de la calculadora. ¡Hasta Luego!")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == 1:
            resultado = suma(num1, num2)
        elif opcion == 2:
            resultado = resta(num1, num2)
        elif opcion == 3:
            resultado = multiplicacion(num1, num2)
        elif opcion == 4:
            resultado = division(num1, num2)
        elif opcion == 5:
            resultado = mod(num1, num2)
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 6.")
            continue

        print("El resultado es:", resultado)

calculadora()
