import os
import time
os.system('cls')


# Fazer um programa que solicita o preço de um produto e
# inflaciona esse preço em 10% se ele for menor que 100 e
# em 20% se ele for maior ou igual a 100.
# Utilize uma função com retorno para obter o resultado solicitado.

def limpa_tela():
    time.sleep(1) # Espera 1 segundos.
    os.system("cls")



def produto(preco, preco_infla):
    if preco >= 100:
        preco_infla=preco+(preco * 0.20)
        return preco_infla
    else:
        preco_infla=preco+(preco*  0.10)


def mostrar_resultado(produto):
      
    print(f"Valor do produto: R$ {produto:.2f}")
    print(f"Valor total: R$ {produto:.2f}")

produto=float(input('Digite o valor de um produto: '))




        