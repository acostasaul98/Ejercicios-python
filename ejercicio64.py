"""caclcular N factorial
"""

n=int(input('Escriba numero: '))
mult=1
for i in range(n+1):
	if i==0:
		continue
	else:
		mult=mult*i
 
print('resultado' ,str(mult))