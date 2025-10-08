import os
import time
os.system('cls')

# Escreva um programa que permita receber do usuário duas
# notas de um aluno e usando duas funções: 
# - Informe por meio de uma função a média;
# - Informe por meio de uma função se a média for maior ou
# igual a 7, o aluno estará aprovado, caso contrário, estará
# reprovado.

# Função para limpar a tela
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)

# Função para calcular a média
def calcular_media(n1, n2):
    return (n1 + n2) / 2

# Função para verificar se foi aprovado ou reprovado
def verificar_aprovacao(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

# Código principal
print('===== BOLETIM =====')
n1 = int(input('Digite a 1ª nota: '))
n2 = int(input('Digite a 2ª nota: '))

# Limpa a tela após a entrada das notas
limpa_tela()

media_final = calcular_media(n1, n2)
resultado = verificar_aprovacao(media_final)

# Exibe os resultados
print(f'A 1ª nota é: {n1}')
print(f'A 2ª nota é: {n2}')
print(f'Média: {media_final}')
print(f'Resultado: {resultado}')
