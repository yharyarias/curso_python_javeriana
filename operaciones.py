numero = 5
print(type(numero))

numero_bool = bool(numero) # convertí la variable "numero" de entero a flotante(decimal)
print(type(numero_bool))

numero_int = int(numero_bool) # Convertí bool a int
print(type(numero_int))

numero_float = float(numero_int)
print(type(numero_float))

# String
cadena_texto_1 = "Clase de Python"
cadena_texto_2 = "en la Javeriana"

frase = cadena_texto_1 + cadena_texto_2
print(frase)
print("---------------")
print(cadena_texto_1, cadena_texto_2)

# Podemos convertir números a texto pero NO
# texto a números.
print(type(str(numero)))
print(numero)
