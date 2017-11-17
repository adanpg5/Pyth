import sys

a = int(sys.argv[1])
mult = 1

if a <= 0:
    sys.exit("Error")

elif a > 0:
    for i in range(1, a + 1):
        mult = mult * i
        print (i, "! =", mult)
