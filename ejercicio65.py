"""
suma de 3 numeros factoriales
"""


import math
lista = [3, 9, 6]
suma = 0
for numero in lista:
	if numero > 0:
		numero = abs(numero)
		suma += math.factorial(numero)
print('Resultado de la suma: ')
print(suma)



 
 