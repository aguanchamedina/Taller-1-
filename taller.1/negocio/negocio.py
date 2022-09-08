#PROGRAMA QUE DE EL TOTAL

from tkinter import mainloop
from  re import  I , T


print("---------------------")
print("--------TOTAL--------")
print("---------------------")

#INPUT
M  = int(input("Ingrese el tipo de Pago: " ))
P  = int(input("Cliente Afiliado, ingrese el precio $: "))
D1 = int
D2 = int
M2 = int ( input("Ingrese el tipo de pago: " ))
P2 = int (input("Cliente General, Ingrese el Precio $: "))
D3 = int
D4 = int
T1 = int
T2 = int


#PROCESS
D1 = (P * 0,20)
D2 = (P * 0,0)

if  M == 1:
    T1 = (P - D1)   
else:
    M == 2
    T1 = (P - D2)


D3 = (P2 * 0.15)
D4 = (P2 * 0.10)

if  M2 == 1:
    T2 = (P2 - D3)
else:
    M2 == 2
    T2 = (P2 - D4)

#OUTPUT
print ("Cliente Afiliado el total es de $: "  + str(T1))
print ("Cliente General el total es de $: "  + str(T2))

#FIN 
mainloop
