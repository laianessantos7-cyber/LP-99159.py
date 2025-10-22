# Escreva um programa que solicite ao usuário o ano de
# nascimento e, utilizando uma função, retorne com a idade do
# usuário.


import os
import time

os.system('cls')

# Criando uma função para calcular a idade
def calcular_idade(ano_nascimento):
    ano_atual = 2025
    return ano_atual - ano_nascimento

# Solicita o ano de nascimento ao usuário
ano = int(input('Digite o seu ano de nascimento: '))

# Calcula e mostra a idade
idade = calcular_idade(ano)
print(f'Você tem {idade} anos.')
