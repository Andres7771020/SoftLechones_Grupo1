#Exameneje1
#Por: Danna Sofia Vargas Quintero
#Servicio Nacional de Aprendizaje SENA
#Script que permita calcular el área de un cuadrado, un rectangulo, trinángulo y un circulo
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print("Nombre:  ", nombre)
print("Apellido: ", apellido)

while True:
    print("Elige una opción para calcular alguna de las figuras geométricas: ")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    print("5. Salir")
    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        lado1 = int(input("Ingrese valor del lado 1 del cuadrado: "))
        lado2 = int(input("Ingrese valor del lado 2 del cuadrado: "))
        print("El área del cuadrado es: ", lado1 * lado2)
    elif opcion == 2:
        base = int(input("Ingrese el valor de la base del rectángulo: "))
        altura = int(input("Ingrese el valor de la altura del rectángulo: "))
        print("El área del rectángulo es: ", base * altura)
    elif opcion == 3:
        base = int(input("Ingrese el valor de la base del triángulo: "))
        altura = int(input("Ingrese el valor de la altura del triángulo: "))
        print("El área del triángulo es: ", 0.5 * base * altura)
    elif opcion == 4:
        radio = float(input("Ingrese el radio del circulo: "))
        print("El área del circulo es: ", 3.1416 * (radio ** 2))
    elif opcion == 5:
        print("Salir")
        break
    else:
        print("Opción no válida")