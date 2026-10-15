if opcion in ('1', '2', '3', '4'):
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == '1':
        print("Resultado:", num1 + num2)
    elif opcion == '2':
        print("Resultado:", num1 - num2)
    elif opcion == '3':
        print("Resultado:", num1 * num2)
    elif opcion == '4':
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            print("Resultado:", num1 / num2)
else:
    print("Opción no válida. Intenta de nuevo.")