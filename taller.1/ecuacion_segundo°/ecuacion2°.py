#PROGRAMA QUE RESUELVE LAS RAICES DE UNA ECUACION DE SEGUNDO GRADO

from tkinter import mainloop

print("---------------------------------------")
print("--------RAICES-DE-SEGUNDO-GRADO--------")
print("---------------------------------------")

#INPUT
A = int(input("Ingrese el valor de A: \n "))
B = int(input("Ingrese el valor de B: \n "))
C = int(input("Ingrese el valor de C: \n "))

#PROCESS
discoteca = ((B ** 2) - (4 * A * C))
R = (discoteca) ** (0.5)

if (discoteca > 0):
    X1 = ((-B) + R) / (2 * A)
    X2 = ((-B) - R) / (2 * A)
    print( "X1= " , X1 )
    print( "X2= " , X2 )
elif ( discoteca == 0 ):
    X1 = ((-B) + R) / (2 * A)
    X2 = ((-B) - R) / (2 * A)
    print("X1= " , X1)
    print("X2= " , X2)

#OUTPUT
else :
    print("Solución imaginaria")

#FIN
mainloop