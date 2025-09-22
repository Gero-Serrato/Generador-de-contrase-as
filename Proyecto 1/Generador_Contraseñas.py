import random
Caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Longitud_contraseña = input("Ingrese la longitud deseada de la contraseña: ")
Contraseña = ""
for i in range(Longitud_contraseña):
    Contraseña += random.choice(Caracteres)
print("tu contraseña es: " (Contraseña))
