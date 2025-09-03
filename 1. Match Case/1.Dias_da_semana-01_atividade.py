#Limpar terminal.
#Atividade 1- 29/08/2025
import os
os.system("cls")


dia= input("Digite um dia da semana: ")

match dia:
    case "1":
        print("Hoje é Domingo.")
    case "2":
        print("Hoje é segunda-feira.")
    case "3":
        print("Hoje é terça-feira.")
    case "4":
      print("Hoje é quarta-feira.")
    case "5":
        print("Hoje é quinta-feira.")
    case "6":
        print("Hoje é sexta-feira.")
    case"sabádo":
        print("Hoje é sabádo.")
    case _:
         print("Dia inválido!")

print(dia)
print("=====FIM====")