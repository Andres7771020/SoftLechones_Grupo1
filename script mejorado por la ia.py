import math

def pedir_texto(mensaje):
    """Valida que el usuario ingrese únicamente letras."""
    while True:
        valor = input(mensaje).strip()
        # Eliminamos los espacios temporalmente por si tiene nombres compuestos (ej: Juan Diego)
        if valor.replace(" ", "").isalpha():
            return valor
        print("Error: Por favor ingrese solo letras válidas.")

def pedir_numero(mensaje):
    """Valida que el usuario ingrese un número mayor a cero."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print(" Error: El valor debe ser mayor a cero.")
        except ValueError:
            print(" Error: Por favor ingrese un número válido, no letras ni símbolos.")

print("="*40)
print("   CALCULADORA DE ÁREAS GEOMÉTRICAS")
print("="*40)

# 1. Capturar y validar nombre y apellido al inicio
nom = pedir_texto("Ingrese su nombre: ").title()
ape = pedir_texto("Ingrese su apellido: ").title()

continuar = "si"

# 2. Ciclo principal para calcular áreas
while continuar == "si":
    print("\nFiguras disponibles: cuadrado, circulo, rectangulo, triangulo")
    figura = input("Ingrese la figura geométrica que desea calcular: ").lower().strip()

    # 3. Uso de elif para controlar el flujo correctamente
    if figura == "cuadrado":
        # Un cuadrado tiene lados iguales, solo necesitamos pedirlo una vez
        lado = pedir_numero("\nIngrese el valor del lado: ")
        area = lado * lado
        print(f" El área del cuadrado es: {area:.2f}")
        
    elif figura == "circulo": 
        # Usamos math.pi para mayor precisión, aunque 3.1416 también es válido
        radio = pedir_numero("\nIngrese el valor del radio: ")
        area = math.pi * (radio ** 2)
        print(f" El área del círculo es: {area:.2f}")
        
    elif figura == "rectangulo":
        base = pedir_numero("\nIngrese el valor de la base: ")
        altura = pedir_numero("\nIngrese el valor de la altura: ")
        area = base * altura
        print(f"El área del rectángulo es: {area:.2f}")
        
    elif figura == "triangulo":
        base = pedir_numero("\nIngrese el valor de la base: ")
        altura = pedir_numero("\nIngrese el valor de la altura: ")
        area = (base * altura) / 2
        print(f" El área del triángulo es: {area:.2f}")
        
    else:
        print(" Figura no reconocida. Revise la ortografía e intente de nuevo.")
        continue # Vuelve al inicio del while sin imprimir el mensaje final

    # Mensaje final de la operación
    print(f"\n El estudiante: {nom} {ape} ha calculado el área de: {figura.capitalize()}")
    
    # 4. Validar la respuesta de continuar
    while True:
        continuar = input("\n¿Desea calcular otra área? (si/no): ").lower().strip()
        if continuar in ["si", "no"]:
            break
        print(" Por favor, responda únicamente con 'si' o 'no'.")

print("\nGracias por usar la calculadora. ¡Hasta pronto!")