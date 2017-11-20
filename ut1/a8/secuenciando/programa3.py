import sys

k = int(sys.argv[1])
cadena = sys.argv[2]

if k < 0:
    sys.exit("Error. Número negativo")

cadenalista = cadena.split()
valor = 0

for palabra in cadenalista:
    if len(palabra) == k:
        valor += 1
print(f"Hay {valor} palabras de tamaño {k}")
