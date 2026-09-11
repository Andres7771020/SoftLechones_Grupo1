# Calculadora de áreas de figuras geométricas
# No se utiliza la librería math

continuar = "S"
while continuar == "S":

    print("\n===================================")
    print("   CALCULADORA DE ÁREAS")
    print("===================================")

    # Validar nombre
    while True:
        nombre = input("Ingrese el nombre: ").strip()

        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Error: el nombre solo debe contener letras.")

    # Validar apellido
    while True:
        apellido = input("Ingrese el apellido: ").strip()

        if apellido.replace(" ", "").isalpha():
            break
        else:
            print("Error: el apellido solo debe contener letras.")

    # Mostrar las figuras disponibles
    print("\nSeleccione una figura:")
    print("1. Círculo")
    print("2. Triángulo")
    print("3. Cuadrado")
    print("4. Rectángulo")

    # Validar la opción del menú
    while True:
        opcion = input("Ingrese una opción (1-4): ")

        if opcion in ["1", "2", "3", "4"]:
            break
        else:
            print("Error: debe seleccionar una opción entre 1 y 4.")

    # Función para validar números positivos
    def pedir_numero(mensaje):
        while True:
            try:
                numero = float(input(mensaje))

                if numero > 0:
                    return numero
                else:
                    print("Error: el número debe ser mayor que 0.")

            except ValueError:
                print("Error: debe ingresar un número válido.")

    # CÍRCULO
    if opcion == "1":

        radio = pedir_numero("Ingrese el radio del círculo: ")

        # π aproximado, sin utilizar math
        pi = 3.1416

        area = pi * radio ** 2

        figura = "círculo"

    # TRIÁNGULO
    elif opcion == "2":

        base = pedir_numero("Ingrese la base del triángulo: ")
        altura = pedir_numero("Ingrese la altura del triángulo: ")

        area = (base * altura) / 2

        figura = "triángulo"

    # CUADRADO
    elif opcion == "3":

        lado = pedir_numero("Ingrese el lado del cuadrado: ")

        area = lado ** 2

        figura = "cuadrado"

    # RECTÁNGULO
    elif opcion == "4":

        base = pedir_numero("Ingrese la base del rectángulo: ")
        altura = pedir_numero("Ingrese la altura del rectángulo: ")

        area = base * altura

        figura = "rectángulo"

    # Mostrar resultado
    print("\n===================================")
    print("             RESULTADO")
    print("===================================")
    print("Nombre:", nombre, apellido)
    print("Figura seleccionada:", figura)
    print("Área:", round(area, 2))
    print("===================================")

    # Preguntar si desea continuar
    while True:

        continuar = input(
            "\n¿Desea calcular otra área? (S/N): "
        ).strip().upper()

        if continuar == "S" or continuar == "N":
            break
        else:
            print("Error: escriba solamente S para continuar o N para finalizar.")


print("\nPrograma finalizado.")
print("Gracias por utilizar la calculadora de áreas.")
