help('keywords')

edad = 27
print(edad)
# type() nos muestra el tipo de datos de las variables
print(type(edad))
# el _ al inicio del nombre de la variable significa
# que esa variable es privada

_nombre_apellido = "yhary arias"

# CONSTANTES 
VELOCIDAD_LUZ = 300000
print(type(VELOCIDAD_LUZ))
GRAVEDAD_TIERRA = 9.8


# Ejemplo de mutabilidad
num_1 = 5
num_2 = num_1 # num_2 = 5

# Dictionary -> key:value
diccionario = {"num": 2, "num1": 3}


# Asiganación aumentada += -= *= /= //= %=
a = 2

b = a + 10 
print(b) # b = 12

# Lo mismo
a = a + 10 # a = 12
a += 10 # reducción de la operación anterior
print(a) # 22
a -= 4
print(a) # 18