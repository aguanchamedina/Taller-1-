#PROGRAMA QUE DETERMINE SI LOS DOS ULTIMOS DIGITOS SON IGUALES

from math import trunc
from tkinter import mainloop

print("---------------------------------------------")
print("--------DOS-ULTIMOS-DIGITOS-IGUALES----------")
print("---------------------------------------------")

#INPUT
X  = int(input( "Ingrese el valor de X: " ))
Y  = int
Y1 = int
Y2 = int

#PROCESS
Y  =  X  %  100
Y1  =  Y  >  10
Y1  =  trunc ( Y / 10 )   
Y2  =  Y  %  10

if  Y1  ==  Y2 :
    msj  =  " Son iguales."
else :
    Y1  !=  Y2
    msj  =  " No son iguales."

#OUTPUT
print ( "Los dos ultimos digitos de: "  +  str(X) +  " son: "  +  str(Y) + 
" Entonces, "  +  str(Y1) +  " y "  + ""+  str (Y2) +  str(msj))

#FIN
mainloop