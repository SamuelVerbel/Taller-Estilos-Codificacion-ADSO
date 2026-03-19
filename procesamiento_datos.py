
def sumar_numeros(numero_uno, numero_dos):
    """Retorna la suma de dos números reales."""
    return numero_uno + numero_dos

def restar_numeros(numero_uno, numero_dos):
    """Retorna la diferencia entre dos números reales."""
    return numero_uno - numero_dos

def multiplicar_numeros(numero_uno, numero_dos):
    """Retorna el producto de dos números reales."""
    return numero_uno * numero_dos

def dividir_numeros(dividendo, divisor):
    """
    Realiza la división protegiendo el programa de errores por cero.
    """
    if divisor == 0:
        return "Error: No es posible dividir por cero."
    return dividendo / divisor

def obtener_modulo(dividendo, divisor):
    """Calcula el residuo de una división entera."""
    if divisor == 0:
        return "Error: No es posible calcular el módulo por cero."
    return dividendo % divisor

def ejecutar_calculadora():
    """Función principal que gestiona la interfaz de usuario de la calculadora."""
    while True:
        print("\n--- CALCULADORA BÁSICA ADSO ---")
        print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Módulo\n6. Salir")
        
        try:
            opcion = int(input("\nSeleccione una operación (1-6): "))
            
            if opcion == 6:
                print("Operación finalizada. ¡Hasta luego!")
                break

            if opcion not in range(1, 7):
                print("Opción no válida. Intente de nuevo.")
                continue

            n1 = float(input("Ingrese el primer número: "))
            n2 = float(input("Ingrese el segundo número: "))

            if opcion == 1:
                resultado = sumar_numeros(n1, n2)
            elif opcion == 2:
                resultado = restar_numeros(n1, n2)
            elif opcion == 3:
                resultado = multiplicar_numeros(n1, n2)
            elif opcion == 4:
                resultado = dividir_numeros(n1, n2)
            elif opcion == 5:
                resultado = obtener_modulo(n1, n2)

            print(f"\nResultado: {resultado}")

        except ValueError:
            print("Error: Por favor, ingrese solo valores numéricos.")

if __name__ == "__main__":
    ejecutar_calculadora()