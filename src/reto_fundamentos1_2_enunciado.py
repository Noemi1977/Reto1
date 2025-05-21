# 🌟 Reto: Gestor de contactos

# 🎯 Objetivo:
# Crear una pequeña aplicación en consola que permita al usuario
# almacenar, mostrar y buscar contactos usando listas y diccionarios.

# Instrucciones:

# 1. Añadir un contacto:
#    - Pide al usuario el nombre, edad y ciudad.


#    - Guarda el contacto en una lista como un diccionario.


# 2. Mostrar todos los contactos:
#    - Recorre la lista y muestra los datos en el formato:
#      Nombre: Marta – Edad: 30 – Ciudad: Oviedo



# 3. Buscar por nombre:
#    - Pide un nombre y muestra el contacto si existe.

# 4. Salir:
#    - Si el usuario elige la opción 4, termina el programa.

# 💡 Menú sugerido:
# ¿Qué quieres hacer?
# 1. Añadir contacto
# 2. Ver contactos
# 3. Buscar por nombre
# 4. Salir

def main():
    # lista de contactos
    contactos = []
    while True:
        print("__________Gestor de contactos__________")
        print("¿Qué quieres hacer?")
        print("1. Añadir contacto")
        print("2. Ver contactos")
        print("3. Buscar por nombre")
        print("4. Salir")
        print("------------------------------------------")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nuevo_contacto(contactos)
        elif opcion == "2":
            ver_contacto(contactos)
        elif opcion == "3":
            buscar_contacto(contactos)
        elif opcion == "4":
            print("Adios!!!!...")
            break
        else:
            print("Opción no válida, prueba otra vez.")

# Añadir contacto
def nuevo_contacto(contactos):
    print("________Añadir nuevo contacto________")
    nombre = input("Nombre: ")
    # introducir un numero para la edad
    while True:
        try:
            edad = int(input("Edad: "))
            if edad <= 0:
                print("la edad tiene que ser mayor que cero")
            elif edad >= 100:
                print("si has llegado hasta aqui eres un maquina")
            else:
                break
        except ValueError:
            print("No es un numero apropiado para la edad")
    ciudad = input("Ciudad: ")

    contacto = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }
    # añadimos a la lista el dicconario
    contactos.append(contacto)
    print("Contacto añadido con éxito.")
    print(contactos)

# Opcion 2 Ver contactos
def ver_contacto(contactos):
    print("----------- Lista de Contactos ----------")
    if not contactos:
        print("No hay contactos a mostrar")
        return

    for c, contacto in enumerate(contactos, 1):
        print(f"{c}.- Nombre: {contacto['nombre']} - Edad: {contacto['edad']} - Ciudad: {contacto['ciudad']}:")
    print("------------------------------------------")
    print("¿Quieres ver otro contacto? (s/n)")
    respuesta = input()
    if respuesta.lower() == "s":
        ver_contacto(contactos)
    else:
        print("Volviendo al menú principal...")
        print("------------------------------------------")

# Opcion 3 Buscar contacto
def buscar_contacto(contactos):
    print("----------- Buscar Contactos ----------")
    if not contactos:
        print("No hay contactos a mostrar")
        return
    dato_buscar = input("Introduce un dato a buscar: ")
    # saber que tipo de dato es 
    encontrado = False
    try:
        dato_n = int(dato_buscar) #si el usuario entroduce un número interpreta que busca la edad
        tipo_busqueda = "n"
    except ValueError:
        # es un string busco en nombre y en ciudad
        tipo_busqueda = "t"

    for d in contactos:
        if (tipo_busqueda == "n" and d["edad"] == dato_n):
            encontrado = True
            print(f"Contacto encontrado: {d}")
            break
        elif (dato_buscar.lower() in d["nombre"].lower() or 
              dato_buscar.lower() in d["ciudad"].lower()):
            encontrado = True
            print(f"Contacto encontrado: {d}")
            break

    if not encontrado:
        print("Contacto NO encontrado")
    print("------------------------------------------")
    print("¿Quieres buscar otro contacto? (s/n)")
    respuesta = input()
    if respuesta.lower() == "s":
        buscar_contacto(contactos)
    else:
        print("Volviendo al menú principal...")
        print("------------------------------------------")
if __name__ == "__main__":
    main()

