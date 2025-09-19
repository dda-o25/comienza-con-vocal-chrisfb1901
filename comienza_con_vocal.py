"""

Christian Alonso Flores Burgos

Fecha
19 de septiembre de 2025

Determinar si una palabra comienza con vocal.

"""


# Declaraciones

# Entradas
palabra= input("Escribe una palabra:")
primera_letra = palabra[0].lower()
vocales= "aeiouáéíóúü"

# Proceso

primera_letra = palabra[0].lower()
vocales= "aeiouáéíóúü"

# Salidas
if primera_letra in vocales:
    print("'" + palabra + "'","comienza con vocal")
else:
    print("'" + palabra + "'", "no comienza con vocal")


