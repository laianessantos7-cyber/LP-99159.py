#Atividade 5- 03/09/2025


#Limpar terminal.
import os
os.system("cls")


print("===== ÁREA DE PAGAMENTO. ====")
produto= float(input("Digite o valor do produto: "))
print("""
1- Pagamento a vista.
2- Pagamento a prazo.
""")
forma=int(input("Escolha a forma de pagamento (1 ou 2): "))


match forma:
     case 1:
#Obtendo  o valor do desconto de 10%.
        desconto= produto* 0.10
        form_pagamento= 'valor a vista'
        valor_total= produto - desconto
        print(f"\nPagamento à vista selecionado.")
        print(f"Valor do produto: R$ {produto:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Valor final: R$ {valor_total:.2f}")


     case 2:
         parcelas = int(input("Digite a quantidade de parcelas (até 6): "))
         valor = produto /6
         if parcelas >=1 and parcelas <=6:
            parcelas = 6
            valor_parcela = produto / parcelas
            pagamento = "à prazo"
            print(f"\nPagamento a prazo selecionado.")
            print(f"Valor do produto: R$ {produto:.2f}")
            print(f"Número de parcelas: {parcelas}")
            print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
            print(f"Valor total: R$ {produto:.2f}")
         else: 
            print("Número de parcelas inválido.")
            


     