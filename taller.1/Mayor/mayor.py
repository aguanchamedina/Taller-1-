#PROGRAMA QUE DETERMINE EL NUMERO MAYOR

from tkinter import mainloop

print("------------------------------")
print("--------NUMERO MAYOR----------")
print("------------------------------")

#INPUT
X  =  int(input("Ingrese el primer valor: "))
Y  =  int(input("Ingrese el segundo valor: "))
Z  =  int(input("Ingrese el tercer valor: "))

#PROCESS
if  X  >  Y  and  X  >  Z :
    msj  =  X
else:
    Y  >  X  and  Y  >  Z 
    msj  =  Y
if  Z  >  X  and  Z  >  Y :
    msj  =  Z

#OUTPUT
print ( "El numero mayor es:"  +  str ( msj ))

#FIN
mainloop