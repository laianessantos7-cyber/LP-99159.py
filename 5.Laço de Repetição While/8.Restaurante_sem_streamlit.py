#Faça um algoritmo que mostre um menu com opções de um cardápio de restaurante para uma pessoa. A pessoa vai escolher o prato desejado.
#Após escolher o prato, o algoritmo deve perguntar ao usuário se ele deseja escolher outro prato. Calcule quanto deve ser pago pelo cliente.

import os
os.system("cls")

print("=====CARDÁPIO====")

print("""
Código \t Prato \t\t Valor
1 \t Picanha \t R$25,00
2 \t Lasanha \t R$20,00
3 \t Strogonoff \t R$18,00
4 \t Bife Acebolado\t R$15,00
5 \t Pão com ovo \t R$ 5,00
      """)

total=0.0

while True:
    codigo= input("Digite o código de um prato: ")
    if codigo == "1":
        total += 25
        print("Você escolheu Picanha")
    elif codigo== "2":
        total += 20
        print("Você escolheu Lasanha")
    elif codigo== "3":
        total += 18
        print("Você escolheu Strogonoff")
    elif codigo== "4":
        total += 15
        print("Você escolheu Bife Acebolado")
    elif codigo == "5":
        total += 5
        print("Você escolheu Pão com Ovo")
    else:
        print("Opção inválida!")
    continuar = input("Deseja escolher outro prato? (s/n): ").lower()
    if continuar != "s":
        break
os.system("cls")


print(f"\nTotal a pagar: R${total:.2f}")
print("Obrigado pela preferência, Volte sempre!")

