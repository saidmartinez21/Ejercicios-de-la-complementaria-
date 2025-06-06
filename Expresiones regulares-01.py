##
# 01 - Expresiones regulares
#

"""
Las expresiones regulares son una secuencia de caracteres que forman un patron de busqueda.
Se utilizan para la búsqueda de cadenas de texto, validacion de datos, etc.

¿Por qué aprender Regex?

Busqueda avanzada 

Validación de datos. Asegurarse que los datos que ingresa el ususario como el email, telefono, etc., son correctos.

Extracción de información. Permite obtener y aprovechar datos especificos de un texto, como nombres, fechas o direcciones.

Manipulación de texto. Extraer, reemplazar y modificar partes de la cadena de texto facilmente. 

"""

#1. Importar el modulo de expresiones regulares "re"
import re

#2. Crear un patron, que es una cadena de texto
# que describe lo que queremos encontrar.
pattern = "Hola"

#3. El texto donde queremos buscar
text = "Hola mundo"

#4. usar la funcion de búsqueda de "re"
result = re.search(pattern, text)

if result:
    print("He encontrado el patrón en el texto")
else:
    print("No he encontrado el patrón en el texto")

# .group() devuelve la cadena que coincide con el patron
print(result.group())

# .start() devuelve la posicion inicial de la conincidencia 
print(result.start())

# .end() devuelve la posicion final de la coincidencia
print(result.end())

# Ejercicio 1
# Encuentra la primera ocurrencia de la palbra "IA" en el siguiente texto e indica en que posicion empieza y termina
# la coincidencia 

pattern = "IA"
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la puede fallar con las regex para ir con cuidado"
result = re.search(pattern, text)

if result:
    print(f"He encontrado el patrón en el texto en la posicion {result.start()} y termina en la posicion {result.end()}")
else:
    print("No he encontrado el patrón en el texto")

#------------------------------------------------------------------------------------------------------------

# Encontrar todas las coincidencias de un patron 
# .findall() Devulve una lista con todas la coincidencias

text = "Me gusta Python. Python es lo maximo. Aunque Python no es tan dificil, ojo con Python"
pattern = "Python"

matches = re.findall(pattern, text)
print(matches)
print(len(matches))

# .finditer() Devuelve un iterador que contiene todos los resultados de la busqueda

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())

### Modificadores 

# los modificadores son opciones que se pueden agregar a un patron para cambiar 
# su comportamiento

#re. IGNORECASE: Ignora las mayusculas y minusculas

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala.Viva la Ia"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)

print(found)