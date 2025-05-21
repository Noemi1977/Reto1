# ------------------------------
# ✨ Ejercicio 1: Saludo básico
# Objetivo: Aprender a definir y llamar funciones
# Crea una función llamada saludar() que imprima: "¡Hola, bienvenido/a!"
# Luego llama a la función una vez para comprobar que funciona.

def saludar():
    print("¡Hola, bienvenido/a!")

saludar()

# ------------------------------
# ✨ Ejercicio 2: Saludo personalizado
# Objetivo: Trabajar con parámetros
# Crea una función llamada saludar_persona(nombre) que imprima: "Hola, [nombre]!"
# Llama a la función dos veces con diferentes nombres.

def saludo_personal(nombre):
    print (f" Hola, {nombre}")

saludo_personal("Emma")

# ------------------------------
# ✨ Ejercicio 3: Suma fácil
# Objetivo: Usar parámetros y return
# Crea una función llamada sumar(a, b) que devuelva la suma de dos números.
# Guarda el resultado en una variable y muéstralo con print().

def suma_facil(a, b):
    resultado= a+b
    return resultado 
print("La suma es: ", suma_facil(5, 10)) 

# ------------------------------
# ✨ Ejercicio 4: ¿Par o impar?
# Objetivo: Usar lógica dentro de una función
# Escribe una función es_par(numero) que devuelva True si el número es par y False si es impar.
# Pruébala con varios números y muestra el resultado.

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False    
    
print("El número 4 es par: ", es_par(4))
print("El número 5 es par: ", es_par(5))


# ------------------------------
# ✨ Ejercicio 5: Mensaje con formato
# Objetivo: Devolver una cadena con formato
# Crea una función llamada mensaje(nombre, edad) que devuelva una frase como:
# "Me llamo Marta y tengo 30 años."
# Usa return y luego muestra el mensaje con print().

def mensaje(nombre, edad):
    return f"Me llamo {nombre} y tengo {edad} años."
print(mensaje("Marta", 30))



# ------------------------------
# ✨ Ejercicio 6: Calculadora simple
# Objetivo: Practicar varias funciones juntas
# Crea 4 funciones: sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b)
# Llama a cada una con un par de números y muestra los resultados.
# Bonus: en dividir(), si el segundo número es 0, devuelve "No se puede dividir por cero"

def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b    
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero" 
    
print("Suma: ", sumar(10, 5))
print("Resta: ", restar(10, 5))


# ------------------------------
# ✨ Ejercicio 7: Edad en el futuro
# Objetivo: Usar return con operaciones
# Escribe una función llamada edad_futura(edad_actual, años) que calcule la edad que tendrás después de X años.

def edad_futura(edad_actual, anos):
    return edad_actual + anos
print("Tu edad en 10 años será: ", edad_futura(30, 10))

# ------------------------------
# ✨ Ejercicio 8: Media de 3 números
# Objetivo: Trabajar con números y return
# Crea una función llamada calcular_media(a, b, c) que devuelva la media de tres números.
# Prueba la función y muestra el resultado con print().

def calcular_media(a, b, c):
    return (a + b + c) / 3
print("La media de 3 números es: ", calcular_media(10, 20, 30))


# ------------------------------
# ✨ Ejercicio 9: Mostrar menú (sin lógica)
# Objetivo: Separar la presentación de la lógica
# Escribe una función llamada mostrar_menu() que imprima un pequeño menú como:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión

def mostrar_menu():
    opciones = ["Ver perfil", "Editar perfil", "Cerrar sesion"]
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

# ------------------------------
# 🌟 Reto Final: Generador de contraseñas

# Crea una función llamada generar_contraseña(longitud)
# que devuelva una contraseña aleatoria con la longitud especificada.

# La contraseña debe contener una mezcla de:
# - letras minúsculas (a-z)
# - letras mayúsculas (A-Z)
# - números (0-9)
# - símbolos como !, @, #, $, %, &, *

# Ejemplo de uso:
# contraseña = generar_contraseña(12)
# print(contraseña)  # -> A2c$e9#Tq&7L

# Bonus:
# - Usa la librería random
# - Controla que la longitud mínima sea 8 caracteres
# - Añade un mensaje de advertencia si se pide menos de 8

def generar_contraseña(longitud):
    import random
    import string

    if longitud < 8:
        return "La longitud mínima es de 8 caracteres."

    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()" # Mezcla de letras, números y símbolos
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud)) # Genera la contraseña aleatoria
    return contraseña