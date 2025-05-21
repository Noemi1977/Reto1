# # Ejercicio 1, identificar tipos básicos
a="Hola";
b=25;
c=3.14;
d=True;
e=None;
print(type(a));
print(type(b));
print(type(c));
print(type(d));
print(type(e));

# # Ejercicio 2, practicar conversiones entre tipos.

cadena="42";
cad_integer= int(cadena);
print(cad_integer);

suma_cad=cad_integer+8;
print(suma_cad);

num=100;
num_cad= str(num);
print("Tu puntuacion es ", num_cad);

# # Ejercicio 3, nombres y saludos

nombre="Noemi";
edad=47;
print ("Hola me llamo ", nombre, "y tengo ", edad, " años");

# # Ejercicio 4, Reasignar valores de forma clara
x="gato";
y="perro";
print("Imprimeme el valor de x: ", x);
print("Imprimeme el valor de y: ", y);

x="perro";
y="gato";

print("Imprimeme el valor de x: ", x);
print("Imprimeme el valor de y: ", y);

# # Ejercicio 5. Suma de la compra

pan= 1.20;
leche=0.95;
huevos=2.10;

total= pan+leche+huevos;
print("El total de tu compra es: ", total);

# # Ejercicio 6. ¿Par o impar?

numero= input("Introduce un numero: ");
if int(numero) % 2 == 0:
    print("El numero es par");
else:
    print("El numero es impar");

# Ejercicio 7. ¿Mayor de edad?
edad= input("Introduce tu edad: ");
if int(edad) >= 18:
    print("Eres mayor de edad");
else:
    print("Eres menor de edad");

# Ejercicio 8. ¿Elige una opción?

seleccion= input("Ingresa una opción del 1 al 3:");
if seleccion == "1":
    print("Ver perfil");
elif seleccion == "2":
    print("Editar perfil");
elif seleccion == "3":
    print("Cerrar sesión")
else :
    print("No has marcado ninguna opcion valida");

# Ejercicio 9. Detector de tipos raros

def verificar_tipo(valor):
    if(isinstance(valor,str)):
        print("El valor introducido es una cadena de texto");
    elif isinstance(valor,int):
        print("El valor introducido es un número entero");
    elif isinstance(valor,float):
        print("El valor introducido es un numero decimal");
    elif isinstance(valor,bool):
        print("El valor introducido es un booleano");
    elif valor is None:
        print("El valor introducido es nulo");
    else:
        print("No reconozco el valor que has introducido");

verificar_tipo("Hola")
verificar_tipo(25)
verificar_tipo(3.14)
verificar_tipo(True)
verificar_tipo(None)

#Otra forma de hacerlo
dato= input("Introduce un dato:")

try:
    if dato.isdigit():
        dato=int(dato)
    elif dato.replace(".","",1).isdigit():
        dato=float(dato)
    verificar_tipo(dato)
except ValueError:
    print("El valor introducido no es un número válido")

# ✨ Ejercicio 10: Calculadora con menú
# Pide dos números y muestra este menú:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# Según la opción elegida, haz la operación y muestra el resultado.
# Bonus: si elige dividir y el segundo número es 0, muestra “No se puede dividir por cero”.

def calculadora():
    number1 = float(input("Introduce el primer número: "))
    number2 = float(input("Introduce el segundo número: "))
    print("Elige una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion = input("Opción elegida: ")
    if opcion == "1":
        resultado = number1 + number2
        print(f"La suma es: {resultado}")
    elif opcion == "2":
        resultado = number1 - number2
        print(f"La resta es: {resultado}")
    elif opcion == "3":
        resultado = number1 * number2
        print(f"La multiplicación es: {resultado}")
    elif opcion == "4":
        if number2 != 0:
            resultado = number1 / number2
            print(f"La división es: {resultado}")
        else:
            print("No se puede dividir por cero.")
    else:
        print("Opción no válida.")

calculadora()        

# ✨ Ejercicio 11: Clasificador de edad
# Pide al usuario su edad y clasifícalo:
# - Menor de 3: “Bebé”
# - Entre 3 y 12: “Infancia”
# - Entre 13 y 17: “Adolescencia”
# - Entre 18 y 64: “Adulto”
# - 100 o más: “Senior”

def age():
    age= int(input("Introduce tu edad: "))
    if age<3:
        print ("Eres un bebe")
    elif age>=3 and age<=12:
        print ("Eres un niño")  
    elif age>=13 and age<=17:
        print ("Eres un adolescente")   
    elif age>=18 and age<=64:
        print ("Eres un adulto")
    elif age>=100:
        print ("Eres un senior")    
    else:
        print ("No tengo clasificacion para tu edad")

age()