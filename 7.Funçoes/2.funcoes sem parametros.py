import os

#Criando uma Função.

def logo_senai(): 
    os.system('cls')
    print('=======')
    print('= SENAI =')
    print('=======')

logo_senai()
nome=input('Digite seu nome: ')
logo_senai()
idade= int(input('Digite sua idade: '))
logo_senai()
peso= float(input('Digite seu peso: '))

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Peso: {peso}')

