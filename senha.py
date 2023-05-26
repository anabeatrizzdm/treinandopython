import random

print("bem vindo ao gerador de senha")

nome = input("qual seu nome? ")

email = input("qual seu email? ")

chars = 'abcdefghijkmnopqrstuvwxyzABDCDEFGHIJKMNOPQRSTUVWXYZ!@$%&*(),.?0123456789'

number = input('quantidade de senhas para gerar: ')
number = int(number)

length = input('digite o tamanho da senha: ')
length = int(length)

print('\naqui esta suas senhas: ')

for senha in range(number):
    senhas = ''
    for c in range(length):
        senhas += random.choice(chars)
    print(senhas)
