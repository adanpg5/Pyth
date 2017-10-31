# ¿Me da cambio por favor?

print ("Bienvenido a la máquina de cambio.")
print ("Disponemos de billetes de: 50€, 20€, 10€ y 5€")
print ("También disponemos de monedas de 1€ y 2€.")
valor_euros = int(input("Sabiendo esto, inserte una cantidad la cual va a cambiar:"))
print(type(valor_euros))

dinero_50 = valor_euros % 50 # la variable dinero_valor mete el resto de la división
dinero_50x = valor_euros // 50 # la variable dinero_valorx es el número de billetes que devuelve

print ("Para", valor_euros, "€, es necesario:")

if dinero_50x > 0:
    print (dinero_50x, "de 50€.")
else:
    print ("")
  
dinero_20 = dinero_50 % 20
dinero_20x = dinero_50 // 20

if dinero_20x > 0:
    print (dinero_20x, "de 20€.")
else:
    print ("")
 
dinero_10 = dinero_20 % 10
dinero_10x = dinero_20 // 10

if dinero_10x > 0:
    print (dinero_10x, "de 10€.")
else:
    print ("")
   
dinero_05 = dinero_10 % 5
dinero_05x = dinero_10 // 5

if dinero_05x > 0:
    print (dinero_05x, "de 5€.")
else:
    print ("")

dinero_02 = dinero_10 % 2
dinero_02x = dinero_10 // 2
    
if dinero_02x > 0:
    print (dinero_02x, "de 2€.")
else:
    print ("")
   
dinero_01 = dinero_02 % 1
dinero_01x = dinero_02 // 1

if dinero_01x > 0:
    print (dinero_01x, "de 1€.")
else:
    print ("")