import sys
from math import pi

radio = float(sys.argv[1])

print("Usted ha elegido un radio de ", radio, "cm.")
print("¿Qué desea hacer?")
print("1.- Calcular el diámetro.")
print("2.- Calcular el perímetro.")
print("3.- Calcular el área.")
print("4.- Salir.")

opcion = int(input("Teclee la opción que usted desee."))

diametro = 2 * radio
perimetro = 2 * pi * radio
area = pi * (radio ** 2)

if opcion == 1:
    print("El diámetro de su circunferencia es: ", diametro)
elif opcion == 2:
    print("El perímetro de su circunferencia es: ", perimetro)
elif opcion == 3:
    print("El área de su circunferencia es: ", area)
elif opcion == 4:
    print("¡Adiós!")
else:
    print("Número incorrecto.")
