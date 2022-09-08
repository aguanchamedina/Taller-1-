#PROGRAMA QUE DETERMINE EL VALOR A PAGAR EN UNA LLAMADA

from tkinter import mainloop

print ("------------------------------")
print ("--------VALOR-A-PAGAR---------")
print ("------------------------------")

#INPUT
X  = int(input("Tiempo de llamada: " ))

#PROCESS
if  X  ==  3 :
    msj  =  300
else :
    X  >  3
    msj  =  300  +  int (( X  -  3 ) *  50 )

#OUTPUT
print("Total a pagar: ""$"  +  str(msj))  

#FIN 
mainloop