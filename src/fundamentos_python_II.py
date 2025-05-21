
# ✨ Ejercicio 1: Lista de la compra
# Crea una lista con al menos 5 elementos. Muestra el primero y el último elemento.

list = ["arbol", "mesa", "ordenador", "coche", "movil"]
 
print("El primer elemento es: ", list[0])
print ("El último elemento es: ", list[-1])

# ✨ Ejercicio 2: Añadir y eliminar
# Añade un nuevo elemento a la lista anterior y elimina otro. Imprime la lista actualizada.

list.append("silla")
list.remove("mesa")
print("Lista actualizada: ", list)

# ✨ Ejercicio 3: Ordenar números
# Crea una lista de números desordenados y ordénala de menor a mayor.

unOrderList= [5, 2, 10, 1, 7, 6]
unOrderList.sort()
print("Lista ordenada: ", unOrderList)

# ✨ Ejercicio 4: Coordenadas
# Crea una tupla con una coordenada (latitud, longitud) y muéstrala.

coordenadas = (40.7578, -32.0060)
print ("Las coordenadas son :", coordenadas)

# ✨ Ejercicio 5: Elemento fijo
# Crea una tupla de 3 elementos. Intenta cambiar uno y observa qué sucede.

elements = (1, 2, 3)
try:
    elements[0] = 4 
except TypeError as e:
    print("Error: ", e)
    print("No se puede cambiar un elemento de una tupla.")

#✨ Ejercicio 6: Diccionario de usuario
# Crea un diccionario con las claves: nombre, edad, ciudad.

dictionary = {
    "nombre": "Noemi",
    "edad": 47,
    "ciudad": "Piedras Blancas"
}

# ✨ Ejercicio 7: Actualizar valores
# Cambia el valor de ciudad y añade una nueva clave llamada email.
dictionary["ciudad"]= "Aviles"
dictionary["email"]= ""

# ✨ Ejercicio 8: Iterar claves y valores
# Imprime cada clave y su valor en una línea distinta.

for key, value in dictionary.items():
    print(f"{key}: {value}")

# ✨ Ejercicio 9: Eliminar duplicados
# A partir de una lista con nombres repetidos, crea un set para mostrar solo los nombres únicos.

nombres = ["Ana", "Luis", "Ana", "Pedro", "Luis"]
nombres_unicos = set(nombres)
print("Nombres únicos: ", nombres_unicos)


# ✨ Ejercicio 10: Operaciones de conjuntos
# Dado dos sets A y B, muestra qué elementos están en A pero no en B.

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

diferencia = set_a - set_b
print("Elementos en A pero no en B: ", diferencia)  

#🌟 Ejercicio Extra: Mezcla total
# Crea un diccionario donde cada clave sea el nombre de una persona y el valor una lista de hobbies.
# Añade un nuevo hobby a una persona y muestra todos los hobbies de otra.   

hobbies = {
    "Noemi": ["pintar", "cocinar"],
    "Falo": ["futbol", "correr"],
    "Hemma": ["leer", "escribir"],
    "Julia": ["pintar", "cocinar"],
    "Satur": ["futbol", "correr"]
}
hobbies["Noemi"].append("leer")
print("Hobbies de Satur: ", hobbies["Satur"])