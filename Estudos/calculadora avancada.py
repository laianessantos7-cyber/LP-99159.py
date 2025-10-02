 #Limpar o terminal.
import math
import os
os.system("cls")

print("===Calculadora Avançada===")
print("Operações disponivéis:")
print("+ -> soma.")
print("- -> subtração.")
print("* -> multiplicação.")
print("/ -> divisão.")
print("%  -> resto da divisão")
print("^  -> potência")
print("sqrt -> raiz quadrada")


#Pedir operação.

operador= input ("Digite operação desejada: ")


#Se for raiz quadrado só precisa de 1 número.

if operador== "sqrt":
        float(input("Digite o número: "))
resultado = math.sqrt(sum)


num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))

if operador == "+":
        resultado = num1 + num2
elif operador == "-":
        resultado = num1 - num2
elif operador == "*":
        resultado = num1 * num2
elif operador == "/":
        if num2 != 0:
            resultado = num1 / num
            
        else:
            resultado = "Erro! Divisão por zero."
elif operador == "%":
        resultado = num1 % num2
elif operador == "^":
        resultado = num1 ** num2
else:
        resultado = "Operador inválido!"

print("Resultado:", resultado)





