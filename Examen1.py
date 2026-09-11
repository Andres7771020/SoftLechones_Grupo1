Nom= (input("ingrese su nombre: "))
Ape= (input("ingrese su apellido: "))
Figura= input("ingrese su figura geometrica: ")
if Figura == "cuadrado":
    Lado1 = float(input("ingrese el valor del lado1: "))
    Lado2 = float(input("ingrese el valor del lado2: "))
    Fc= Lado1 * Lado2
    print("el area del cuadrado es: ", Fc) 
else:
    if Figura == "circulo": 
        Pi= 3.1416
        radio= float(input("ingrese el valor del radio: "))
        Fcir= Pi * (radio ** 2)
        print("el area del circulo es: ", Fcir)
if Figura == "rectangulo":
    Base= float(input("ingrese el valor de la base: "))
    Altura= float(input("ingrese el valor de la altura: "))
    Far= Base * Altura
    print("el area del rectangulo es: ", Far)
else:
    if Figura == "triangulo":
        Base_t= float(input("ingrese el valor de la base: "))
        Altura_t= float(input("ingrese el valor de la altura: "))
        Fat= (Base_t * Altura_t) / 2
        print("el area del triangulo es: ", Fat)
print("El estudiante: ", Nom, "", Ape, "ha calculado el area de:", Figura)
continuar= input("desea calcular otra area? (si/no): ")
while continuar == "si":
    Figura= input("ingrese su figura geometrica: ")
    if Figura == "cuadrado":
        Lado1 = float(input("ingrese el valor del lado1: "))
        Lado2 = float(input("ingrese el valor del lado2: "))
        Fc= Lado1 * Lado2
        print("el area del cuadrado es: ", Fc) 
    else:
        if Figura == "circulo": 
            Pi= 3.1416
            radio= float(input("ingrese el valor del radio: "))
            Fcir= Pi * (radio ** 2)
            print("el area del circulo es: ", Fcir)
    if Figura == "rectangulo":
        Base= float(input("ingrese el valor de la base: "))
        Altura= float(input("ingrese el valor de la altura: "))
        Far= Base * Altura
        print("el area del rectangulo es: ", Far)
    else:
        if Figura == "triangulo":
            Base_t= float(input("ingrese el valor de la base: "))
            Altura_t= float(input("ingrese el valor de la altura: "))
            Fat= (Base_t * Altura_t) / 2
            print("el area del triangulo es: ", Fat)
    print("El estudiante: ", Nom, "", Ape, "ha calculado el area de:", Figura)
    continuar= input("desea calcular otra area? (si/no): ")
    


