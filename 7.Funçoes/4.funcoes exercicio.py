import os
os.system('cls')
#Função com passagem de parâmetros.
#Criando uma Função.


#- Função: 
def saudacao(nome, idade, peso, altura): 
    print(f'Olá, {nome}! Bem-vindo(a) ao nosso site. ')
    print(f'Sua idade é {idade} anos.')
    print(f'Seu peso  é {peso}.')
    print(f'Sua altura é {altura}.')


print('Solicitando dados')   
nome=input('Digite seu nome: ')
idade=int(input('Digite sua idade: '))
peso=float(input('Digite seu peso:'))
altura=float(input('Digite sua altura: '))
#Chamando função.
saudacao(nome, idade, peso, altura)




