import sys

dni = int(sys.argv[1])

resto = dni % 23
lista = "TRWAGMYFPDXBNJZSQVHLCKE"
letra = lista[resto]

print(f"{dni}{letra}")
