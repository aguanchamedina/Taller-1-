#Verificar si el ultimo digito de un numero es par.

from tkinter import mainloop

#INPUT
X  =  int ( input ( " Digite el valor de x: " ))

#PROCESS
ultimo_digito  =  X  %  10 
R  =  ultimo_digito  %  2 

#OUTPUT
if  R  ==  0 :
    print ( "El ultimo digito de: "  +  str ( X ) + "," "es PAR" )

#FIN 
mainloop