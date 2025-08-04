import random
import string as s

def generar_contraseña():
    chars = s.ascii_letters + s.digits + s.punctuation
    return ''.join(random.choice(chars) for x in range(12))

password = generar_contraseña()
print(password)

intento = input("introduce una contraseña: ")
if intento == password:
    print("contraseña correctaaaaa")
else:
    print("contraseña incorrecta")