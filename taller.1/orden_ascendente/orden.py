#PROGRAMA QUE DETERMINE EL ORDEN MAYOR A MENOR

from tkinter import mainloop

print("-------------------------------------")
print("--------ORDEN-MAYOR-A-MENOR----------")
print("-------------------------------------") 

#INPUT
X = int(input("Ingrese el valor de X: "))
Y = int(input("Ingrese el valor de Y: "))
Z = int(input("Ingrese el valor de Z: "))

#PROCESS
if  X > Y and Y > Z:
    msj = X, Y, Z
elif Y > X and X > Z:
    msj = Y, X, Z
elif Z > X and Z > Y:
    msj = Z, X, Y
elif Z > Y and Y > X:
    msj = Z, Y, X
elif X > Z and Z > Y:
    msj = X, Z, Y
elif Y > Z and Z > X:
    msj = Y, Z, X
else:
     X == Y == Z
     msj = "numeros iguales"

#OUTPUT
print ("El orden de mayor a menor es: "  +  str(msj))

#FIN 
mainloop