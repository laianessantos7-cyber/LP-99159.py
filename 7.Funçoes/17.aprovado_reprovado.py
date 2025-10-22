# Escreva um programa que permita ler 2 notas de um aluno e informe por meio de funções: A média;
# Com base na média, se o aluno está aprovado ou reprovado.
# Critério para aprovação: média 7,0.

import os
import time

os.system('cls')
lista_notas=[]

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)

# Função para calcular a média
def calcular_media(lista_notas):
    resultado = sum(lista_notas) /3
    return resultado

# Função para verificar se foi aprovado ou reprovado
def resultado_final(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

# Código principal

for i in range(3): 
    while True: 
        nota=float(input(f'Digite a {i+1} nota: '))
        if nota >=0 and nota <=10:
            lista_notas.append(nota)
        else:
         print(' Tente novamente! Informe uma nota válida: ')
         time.sleep(2)
         break
# Limpa a tela após a entrada das notas
limpa_tela()

media_final = calcular_media(lista_notas)


# Exibe os resultados

print('===== RESULTADO FINAL =====')
print(f'Média: {media_final}')
