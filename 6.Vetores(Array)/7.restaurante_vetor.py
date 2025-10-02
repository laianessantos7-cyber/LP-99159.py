import os
os.system('cls')
# Faça um algoritmo que mostre um menu com opções de um cardápio de restaurante para uma pessoa. A pessoa vai escolher o prato desejado. Após escolher o prato, o algoritmo deve perguntar ao usuário se ele deseja escolher outro prato.
# Quando o usuário não quiser mais realizar pedidos, mostre o nome e o valor dos pratos escolhidos e calcule o valor  total da conta.



lista_pratos = []
precos_pratos = []



print("=====CARDÁPIO====")
while True:
    opcao = int(input("""
Código       Prato          Valor
   1        Picanha         R$ 25,00
   2        Lasanha         R$ 20,00
   3        Strogonoff      R$ 18,00
   4        Bife acebolado  R$ 15,00
   5        Pão com ovo     R$ 5,00
                     
Digite a opção desejada: """))
   
    match opcao:
        case 1:
            prato = "Picanha"
            preco = 25
        case 2:
            prato = "Lasanha"
            preco = 20
        case 3:
            prato = "Strogonoff"
            preco = 18
        case 4:
            prato = "Bife acebolado"
            preco = 15
        case 5:
            prato = "Pão com ovo"
            preco = 5
        case _:
            print("Opção inválida. \nTente novamente.\n")
   
    if opcao >= 1 and opcao <= 5:
        lista_pratos.append(prato)
        precos_pratos.append(preco)

    continuar = input("Deseja escolher outro prato? \nResponda com S ou N: ").lower()
    if continuar == "n":
        break
    os.system("cls")

if sum(precos_pratos) == 0:
    print("\nNenhum prato foi escolhido")
else:
    print("\n=PRATOS ESCOLHIDOS=")
    for prato in lista_pratos:
        print(f"Prato: {prato}")

    print(f"\nTotal: R$ {sum(precos_pratos):.2f}")


print("\n Obrigado pela preferência, Volte sempre!")

