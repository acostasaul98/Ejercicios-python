"""
Numero fatorial si es 0 arrojar un 0
"""
n2=int(input('Escriba numero: '))
if n2==0:
    print('Resulatdo ', str(n2))
    
else:
    
    mult=1
for i in range(n2+1):
 
	if i==0:
		continue
	else:
		mult=mult*i
 
print('resultado' ,str(mult))

