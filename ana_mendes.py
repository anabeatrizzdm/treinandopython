print("Ola")
#:calculo volume esfera raio
raio= float(input("Digite o valor do raio: "))

import math
from statistics import median
volume= (4 * math.pi * raio**3) /3
print(f"O volume de uma esfera de raio R é igual a {volume:.2f}")

#:lista de números em ordem crescente
print("olá")
n1= int(input("Digite seu primeiro número: "))
n2= int(input("Digite seu segundo número: "))
n3= int(input("Digite seu terceiro número: "))

if n1 < n2 < n3:
    print(f"A ordem crescente é {n1, n2, n3}")
elif n2 < n3 < n1:
    print(f"a ordem crescente é {n2, n3, n1}")
elif n1< n3< n2:
    print(f"a ordem crescente é {n1, n3, n2}")
elif n2< n1< n3:
    print(f"a ordem crescente é {n2, n1, n3}")
elif n3> n2> n1:
    print(f"a ordem crescente é {n3, n2, n1}") 
elif n3< n1< n2:
    print(f"a ordem crescente é {n3, n1, n2}")

#: exercicio 3

ct= 0
soma= 0
x= 0
print("Digite [0] para sair.")
while True:
    numero= float(input("Digite um número: "))
    if numero == 0:
        break
    if numero> 10:
        x= x+1
    ct= ct+1
    soma= soma + numero
media= soma/ ct
porcentagem= (100* x)/ct
print(f"a quantidade de números digitados foi {ct}\n a soma dos valores digitados é {soma}\n a média aritmética dos valores digitados é {media}\n a porcentagem dos valores acima de 10 digitados é {porcentagem}")
 

