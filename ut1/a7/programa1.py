import sys

a = int(sys.argv[1])

if a <= 0:
    sys.exit("Error")

elif a > 0:
    for i in range(2, a):
        resto = a % i
        if resto == 0:
            print ("No es primo.")
            break
    else:
        print ("Es primo.")
