# Escreva um programa que permita ler 3 notas de
# um aluno, usando laço de repetição e informe por
# meio de uma função a média;

import os
import time

os.system('cls')

# limpar a tela
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)

# Função para calcular a média
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

# Código principal
print('===== BOLETIM =====')

# Lendo as 3 notas com laço
notas = []
for i in range(1, 4):
    nota = float(input(f'Digite a {i}ª nota: '))
    notas.append(nota)

# Limpa a tela após as notas
limpa_tela()

# Calcula a média
media_final = calcular_media(notas[0], notas[1], notas[2])

# os resultados
print('===== RESULTADO FINAL =====')
print(f'Notas: {notas[0]}, {notas[1]}, {notas[2]}')
print(f'Média: {media_final:.1f}')
