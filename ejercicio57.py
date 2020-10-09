"""
Calcular promedio de n numeros
"""

def lee_entero():
    numero = -1
    while numero < 0:
        try:
            numero = int(input("Introduce tu calificacion (-1 finaliza): "))
            if numero==-1:
                return -1
        except:
            print ("\tError, no es un entero")
            pass
    return numero
 
numeros=[]
entrada=0
while entrada!=-1:
    entrada = lee_entero()
    if entrada!=-1:
        numeros.append(entrada)
 
media=float(sum(numeros)) / max(len(numeros), 1)
print("\n-----------------------------------------------------\n")

print("El promedio  es: {}".format(round(media,2)))

print("\n-----------------------------------------------------\n")