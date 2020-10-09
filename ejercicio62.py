def lee_entero():
    numero = -1
    while numero < 0:
        try:
            numero = int(input("Introduce un valor entero (-1 finaliza): "))
            if numero==-1:
                return -1
        except:
            print("\tError, no es un entero")
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
print("Numeros entrados: {}".format(", ".join(map(str, numeros))))
print("La suma es: {}, y la media es: {}".format(sum(numeros), round(media,2)))