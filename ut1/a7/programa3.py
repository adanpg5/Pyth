import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

if a <= 0 or b <= 0:
    sys.exit("Error")

else:
    if a < b:
        for i in range(a, 0, -1):
            if a % i == 0:
                if b % i == 0:
                    print("El máximo común divisor es:", i)
                    break

    elif a == b:
        print("El máximo común divisor es:", a)

    else:
        for i in range(b, 0, -1):
            if b % i == 0:
                if a % i == 0:
                    print("El máximo común divisor es:", i)
                    break
