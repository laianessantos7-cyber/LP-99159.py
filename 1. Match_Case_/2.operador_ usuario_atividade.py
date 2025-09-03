#Limpar terminal.

#Atividade 2- 29/08/2025
import os
os.system("cls")


num1 = float(input("Digite o primeiro número: "))
operador= input("Digite a operação (+,-,*,/): ")
num2 = float (input("Digite o segundo número: "))



soma = num1+num2
subtracao = num1-num2
multiplicacao = num1*num2
divisao = num1/num2 

match operador:
     case "+ ":
          print(f"O operador escolhido foi {operador}. ")
          print(f"O resultado de {num1} e {num2} é igual {soma}")
match operador:
     case "-":
          print(f"O operador escolhido foi {operador}. ")
          print(f"O resultado de {num1} e {num2} é igual {subtracao}: ")
match operador:
     case "*":
          print(f"O operador escolhido foi {operador}. ")
          print(f"O resultado de {num1} e {num2} é igual {divisao}: ")
match operador:
     case "/":
          print(f"O operador escolhido foi {operador}. ")
          print(f"O resultado de {num1} e {num2} é igual {multiplicacao}: ")




