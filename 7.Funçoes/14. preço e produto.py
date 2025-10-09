import os
import time
os.system('cls')


# Fazer um programa que solicita o preço de um produto e
# inflaciona esse preço em 10% se ele for menor que 100 e
# em 20% se ele for maior ou igual a 100.
# Utilize uma função com retorno para obter o resultado solicitado.


def limpa_tela():
    time.sleep(1) #Esperar 1 segundo
    os.system("cls" if os.name == "nt" else "clear")


# Função com parâmetros e com retorno.
def inflacionar_preco(preco):
    if preco >= 100:
        return preco + (preco * 0.20)
    else:
        return preco + (preco * 0.10)

print("===== ÁREA DE PAGAMENTO. ====")

def mostrar_resultado(preco_original, preco_final):
    print(f"Valor original do produto: R$ {preco_original:.2f}")
    print(f"Valor após inflação: R$ {preco_final:.2f}")

# Codigo principal
limpa_tela()  # Chamando a função.
preco = float(input('Digite o valor de um produto: R$ '))
preco_final = inflacionar_preco(preco)
mostrar_resultado(preco, preco_final)



        