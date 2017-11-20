import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = "".join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

A = 0
T = 0
G = 0
C = 0

for i in range(0, DNA_SIZE):
    if sequence[i] == "A":
        A = A + 1
    elif sequence[i] == "T":
        T = T + 1
    elif sequence[i] == "G":
        G = G + 1
    elif sequence[i] == "C":
        C = C + 1
print(f"Adenine = {A}\nGuanine = {G}\nCytosine = {C}\nThymine = {T}")
