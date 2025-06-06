###
# 02 - Metacarcteres 
# los metacaracteres son simbolos especiales con significados especificos en las expresiones generales
###

import re

#1. El punto (.)
# coincidir con cualquier caracter excepto una nueva linea

text = "El granjero salio de su casa con sus compañeros de caza para ir al bosque."
pattern = "ca.a"
found = re.findall(pattern, text)

if (found):
    print(found)
else:
    print("No se ha encontrado el patron")
#Como uswar la barra invertida para anular el significado especial de un simbolo
pattern = r"\."

matches = re.findall(pattern, text)

print(matches)

#2.  \d: conincide con cualquier digito (0-9)

text = "Mi numero de telefono es 0984734678"
pattern = r"\d{10}"
found = re.findall(pattern, text)
print(found)

#3.  \w: coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)

text = "Hotorrinolaringologo_80"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

#4. \s Coincide con cualquier espacio en blanco (espacio, tabulacion, salto de linea)

text = "Hola mundo \n ¿como estas?\t"
pattern = r"\s"
found = re.findall(pattern, text)
print(found)

#5. ^: Coincide con el principio de una cadena
username = "423_Leonel122"
pattern = r"^\w"
valid = re.search(pattern, username)
if valid:
    print("El nombre de usuario es valido")
else:
    print("El numero de usario no es valido")

phone = "+52 767 108 5853"
pattern = r"^\+\d{1,3}"
valid = re.search(pattern, phone)
if valid:
    print("El telefono es valido")
else:
    print("El telefono no es valido")

# $: coincide con el final de una cadena 

text = "Hola mundo mundial"
pattern = r"mundo$"
valid = re.search(pattern, text)
if valid:
    print("La cadena es valido")
else:
    print("La cadena no es valido")

#Ejercicio: Valida un correo que sea del IT de Cd. Altamirano

#Ejercicio. Tenemos una lista de archivos que necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf leonel.webp secret.txt"

# 7. \b. Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"
valid = re.findall(pattern, text)
print(valid)

# |: coincidir con una ccion u otra
frutas = "platano, piña, manzana, aguacate, pera, uva, durazno"
pattern = r"uva|p..a|\b\w{7}\b"
valid = re.findall(pattern, frutas)
print(valid)