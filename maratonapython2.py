hat_list = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no hat.

hat_list[2]= int(input("digite um numero para substituir o meio da lista"))

del hat_list[4]

print(len(hat_list))

print (hat_list) 

my_list = []  # Criando uma lista vazia.
 
for i in range(5):
    my_list.insert(0, i + 1)
 
print(my_list)
 
beatles = []

print("Etapa 1:", beatles)

integrantes = ["john lennon", "Paul", "George"]
beatles.extend(integrantes)

print("Etapa 2:", beatles)

for i in range(2):
    elemento = input("Digite o elemento: ")
    beatles.append(elemento)

print("Etapa 3:", beatles)

beatles.pop(3)

print("Etapa 4:", beatles)

beatles.insert(0, "ringo starr")

print("Etapa 5:", beatles)

("o fabuloso", len(beatles))
