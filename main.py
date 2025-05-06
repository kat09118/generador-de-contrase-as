
import random as r 

#variables 

caracteres = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
contraseña = ""

cc=int(input("cuantos caracteres desearias q tenga tu contraseña"))

# bucle for
for i in range(cc):
    character = r.choice(caracteres)
    contraseña = contraseña+character
print(contraseña) 

