import os
os.system('cls')
# Faça um algoritmo que mostre um menu com opções de um cardápio de restaurante para uma pessoa. A pessoa vai escolher o prato desejado. Após escolher o prato, o algoritmo deve perguntar ao usuário se ele deseja escolher outro prato.
# Quando o usuário não quiser mais realizar pedidos, mostre o nome e o valor dos pratos escolhidos e calcule o valor  total da conta.
lista_prato=[]
lista_preco=[]
total=[]


print("=====CARDÁPIO====")


print("""
Código \t Prato \t\t Valor
1 \t Picanha \t R$25,00
2 \t Lasanha \t R$20,00
3 \t Strogonoff \t R$18,00
4 \t Bife Acebolado\t R$15,00
5 \t Pão com ovo \t R$ 5,00

""")

codigo= input("Digite o código de um prato: ")

match codigo:
    case "1":
        print("Picanha: R$25,00.")
        preco=25
    case "2":
        print("Lasanha: R$20,00.")
        preco=20
    case "3":
        print("Strogonoff: R$18,00.")
        preco=18
    case "4":
      print("Bife Acebolado: R$15,00.")
      preco=15
    case "5":
        print("Pão com ovo: R$ 5,00 ")
        preco=5

    case _: 
        print("Prato indisponível! ")

    
lista_prato.append
lista_preco.append

continuar = input("Deseja escolher outro prato? (s/n): ").lower()
if continuar != "s":
 
    os.system("cls")


print("\nTotal a pagar: R${total: }")
print("Obrigado pela preferência, Volte sempre!")

