import sys
import math

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])
x3 = float(sys.argv[5])
y3 = float(sys.argv[6])

distancia12 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
distancia13 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

if distancia12 < distancia13:
    print(
        "El punto más cercano a (", x1, ",", y1,
        ") es (", x2, ",", y2, ") y está a una distancia de ",
        distancia12
    )
else:
    print(
        "El punto más cercano a (", x1, ",", y1,
        ") es (", x3, ",", y3, ") y está a una distancia de ",
        distancia13
    )
