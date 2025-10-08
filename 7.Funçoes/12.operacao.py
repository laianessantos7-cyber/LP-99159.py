import os
import time
os.system('cls')


# Crie funções que recebam 2 números e retorne a soma,
# subtração, divisão e a multiplicação destes dois números
# informados:
# Obs.: Crie uma função para cada operação.


# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(3) # Espera 3 segundos.
    os.system("cls")

# Função com parâmetros e com retorno.
def somar(n1, n2):
    return n1 + n2

def subr(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def divi(n1, n2):
    # return  n1 / n2 if n2 != 0 else "Divisão por zero."
    if n2 == 0:
        print("Divisão por zero.")
    else:
        return n1 / n2

def mostrar_resultado(posicao1, posicao2, posicao3, posicao4):
    print(f"Soma: {posicao1}")
    print(f"Subtração: {posicao2}")
    print(f"Multiplicação: {posicao3}")
    print(f"Divisão: {posicao4}")


# Código principal.
limpa_tela() # Chamando a função.

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

# Chamando as funções.
soma = somar(primeiro_numero, segundo_numero)
subtracao = subr(primeiro_numero, segundo_numero)
multiplicao = mult(primeiro_numero, segundo_numero)
divisao = divi(primeiro_numero, segundo_numero)

mostrar_resultado(soma, subtracao, multiplicao, divisao)