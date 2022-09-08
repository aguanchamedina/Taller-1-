#PROGRAMA QUE DETERMINE SI UN NUMERO ES ENTERO POSITIVO DE 4 DIGITOS


from tkinter import mainloop


print("-----------------------------------------------------")
print("--------NUMERO ENTERO POSITIVO DE 4 DIGIROS----------")
print("-----------------------------------------------------")
 
#INPUT
X  =  int ( input ( "Ingrese el valor de X: " ))

#PROCESS
X
if  X  >  0  and  X  >  999 :
    msj  =  X
else:
    X  <  0  and  X  >  999 
    mensaje  =  "Error"

#OUTPUT
print ( "El numero es entero positivo de 4 digitos: "  +  str ( msj ))

#FIN
mainloop