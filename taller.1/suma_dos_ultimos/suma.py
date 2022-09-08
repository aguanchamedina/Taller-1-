#PROGRAMA QUE DETERMINE SI LA SUMA DE LOS DOS ULTIMOS DIGITOS ES UN NUMERO DE 1 DIGITO

from math import trunc
from tkinter import mainloop

print("---------------------------------------------------------------------")
print("--------LA-SUMA-DE-LOS-DOS-ULTIMOS-ES-UN-NUMERO-DE-1-DIGITO----------")
print("---------------------------------------------------------------------")


#INPUT
X = int(input( "Ingrese el valor de X: " ))
Y = int
A = int
B = int
S = int

#PROCESS 
Y = X % 100
A = Y > 10
A = trunc (Y / 10)   
B = Y % 10
S = (A  +  B)

if S <= 9:
    msj = S
else:
    S > 10
    mensaje = " Error"

#OUTPUT
print ( "Los dos ultimos digitos de "  + str(X) +  " son: "  + str(Y) + 
" entonces "  + str(A) +  "+"  + str(B) +  " es="  +  str(msj))

#FIN 
mainloop