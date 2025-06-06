import re

#Ejercicio 1: Valida un correo que sea del IT de Cd. Altamirano
correo = "L6692048@cdaltamirano.tecnm.mx"
pattern = r"^L\d{8}@cdaltamirano\.tecnm\.mx$"
valid = re.search(pattern, correo)
if valid:
    print("El correo ha sido validado")
else:
    print("El correo es invalido")

#Ejercicio 2: Tenemos una lista de archivos que necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf leonel.webp secret.txt"
pattern = r"\b\w{1,100}\.txt\b"
valid = re.findall(pattern, files)
if valid:
    print("Los ficheros con extencion .txt son:", (valid))
else:
    print("No se encontraron ficheros con esa extencion")

#Ejercicio 3: Convinaciones de petrones
animales = "Perro, Gato, Lobo, Burro, Venado,Serpiente,Cerdo Dinosaurio, Pescado, Pichon, Perico, Cotorro, Iguana"
pattern = r"P\w{1,20}|\b\w{1,20}\b"
valid = re.findall(pattern, animales)
print(valid)