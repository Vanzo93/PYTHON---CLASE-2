def accion_a():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 + num2
    print("La suma de los dos números es:", resultado)

def accion_b():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 * num2
    print("El producto de los dos números es:", resultado)

def main():
    while True:
        opcion = int(input("Ingrese 1 para realizar la acción A, 2 para realizar la acción B o 0 para salir: "))
        
        if opcion == 1:
            accion_a()
        elif opcion == 2:
            accion_b()
        elif opcion == 0:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor ingrese 1, 2 o 0 para salir.")

if __name__ == "__main__":
    main()
