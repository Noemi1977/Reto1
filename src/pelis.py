import os
import csv
from pathlib import Path

FICHERO = "votos.csv"

# ---------- utilidades ----------
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpiar pantalla

# ---------- persistencia ----------
def cargar_datos():
    peliculas = []
    if Path(FICHERO).exists():
        with open(FICHERO, newline="", encoding="utf-8") as f:# abrir el fichero
            # leer el contenido del fichero
            # DictReader lee el CSV y lo convierte en un diccionario
            reader = csv.DictReader(f)
            peliculas = [row | {"votacion": int(row["votacion"])} for row in reader] # convertir la votación a int
    return peliculas

def guardar_datos(peliculas): # guardar los datos en el fichero
    with open(FICHERO, "w", newline="", encoding="utf-8") as f:
        campos = ["titulo", "votacion"] # campos del CSV
        # DictWriter escribe el CSV a partir de un diccionario
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader() # escribir la cabecera
        writer.writerows(peliculas) # escribir las filas

# ---------- acciones de menú ----------
def añadir_pelicula(peliculas): 
    limpiar_pantalla() 
    print("——— Añadir nueva película ———")
    titulo = input("Título: ").strip() # eliminar espacios en blanco
    if any(p["titulo"].lower() == titulo.lower() for p in peliculas): # comprobar si la película ya existe
        print(f"La película '{titulo}' ya existe.")
    else:
        peliculas.append({"titulo": titulo, "votacion": 0}) # añadir la película a la lista
        print(f"'{titulo}' añadida.")
    input("\nEnter para continuar…")

def votar_pelicula(peliculas): 
    limpiar_pantalla()
    print("——— Votar película ———")
    if not peliculas:
        print("No hay películas para votar.")
    else:
        for idx, p in enumerate(peliculas, 1): # enumerar las películas
            print(f"{idx}. {p['titulo']}  —  votos: {p['votacion']}") # mostrar el índice y la votación
        try:
            idx = int(input("ID de la película a votar: ")) - 1 # restar 1 para que coincida con el índice de la lista
            peliculas[idx]["votacion"] += 1 # incrementar la votación
            print(f"¡Has votado '{peliculas[idx]['titulo']}'!") 
        except (ValueError, IndexError):        # ValueError: no número / IndexError: fuera de rango
            print("ID no válido.")
    input("\nEnter para continuar…")

def mostrar_resultados(peliculas):
    limpiar_pantalla()
    print("——— Resultados ———")
    if not peliculas:
        print("Aún no hay películas.")
    else:
        for p in sorted(peliculas, key=lambda x: x["votacion"], reverse=True): # ordenar por votación
            print(f"{p['titulo']}: {p['votacion']} voto(s)") # mostrar la película y la votación
    input("\nEnter para continuar…")

# ---------- programa principal ----------
def main():
    peliculas = cargar_datos()
    while True:
        limpiar_pantalla()
        print("__________ Gestor de Películas __________")
        print("1. Añadir película")
        print("2. Votar película")
        print("3. Mostrar resultados")
        print("4. Salir")
        print("-----------------------------------------")
        opcion = input("Elige una opción: ").strip() # eliminar espacios en blanco

        if opcion == "1":
            añadir_pelicula(peliculas)
        elif opcion == "2":
            votar_pelicula(peliculas)
        elif opcion == "3":
            mostrar_resultados(peliculas)
        elif opcion == "4":
            guardar_datos(peliculas)
            print("¡Ciao!")
            break
        else:
            print("Opción no válida.")
            input("Enter para continuar…")

if __name__ == "__main__": # si el script se ejecuta directamente
    main() # ejecutar el programa

    
    
