# Ejercicio 1 de listas

# 1. Imprimir el nombre completo con apellidos, letra por 
# letra de forma vertical
 
# Ejemplo:

palabra = "gato"
print(palabra) # Cuando queremos imprimir de forma horizontal

# Cuando queremos imprimir de forma vertical usamos un for
for letra in palabra:
    print(letra)


# 2. Perdile al usuario que ingrese una frase y luego vamos a retornar
# o imprimir el numero de palabras de esa frase (añadir un mensaje)

# Contador de palabras

# input() - Pedirle datos al usuario
# split() - Dive cadenas de texto, por defecto las divide en espacios

frase_inicial = "el método split por defecto divide cadenas de texto por espacios"
palabras_div = frase_inicial.split()
print(palabras_div)


# 3. Tabla de multiplicar:

# Crear un programa que pida un número al usuaro
# e imprima la tabla de multiplicar correspondiente

# input() - Pedir el numero de la tabla
# crear un ciclo for
# imprimir resultado
# range(start, stop, step)


tabla = 4




























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































for i in range(1, 11):
    resultado = tabla * i
    print(tabla, "x", i, "=", resultado)
    

