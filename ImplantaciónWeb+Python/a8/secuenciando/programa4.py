import sys

listanum = sys.argv[1:]
totalnum = len(listanum)
suma = 0

for i in range(0, totalnum):
	suma += float(listanum[i])
media = suma / totalnum
print(f"La media es {media}")
