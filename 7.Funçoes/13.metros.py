import os
import time
os.system('cls')


# Fazer um programa que solicita um valor em metros e por meio de uma função, retorna o correspondente em centímetros.

# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(1) # Espera 3 segundos.
    os.system("cls")

# Função com parâmetros e com retorno.
def calclular(n1):
    return n1 * 100

def mostrar_resultado(centimetros):
    print(f"Centimetros: {centimetros}")

# Código principal.
limpa_tela() # Chamando a função.

cm= float(input("Quantos metros: "))
centimetros=calclular(cm)
mostrar_resultado(centimetros)