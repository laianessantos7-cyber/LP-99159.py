#Atividade 3- 03/09/2025


#Limpar terminal.
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

codigo= input("Digite o código de um prato: ")

match codigo:
    case "1":
        print("Picanha: R$25,00.")
    case "2":
        print("Lasanha: R$20,00.")
    case "3":
        print("Strogonoff: R$18,00.")
    case "4":
      print("Bife Acebolado: R$15,00.")
    case "5":
        print("Pão com ovo: R$ 5,00 ")

    case _: 
        print("Prato indisponível! ")
    