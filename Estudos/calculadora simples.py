# Calculadora.


#Limpar o terminal.

import os
from unittest import result 
os.system("cls")

print("=== Calculadora Simples ===")

#Pedir os números.
print("")

num1 = float(input("Digite o primeiro número: "))
operador= input("Digite a operação (+,-,*,/): ")
num2 = float (input("Digite o segundo número: "))

soma = num1+num2
subtracao = num1-num2
multiplicacao = num1*num2
divisao = num1/num2 


#Fazer a operação.

if operador== "+":
    result == num1 + num2 

elif operador == "-":
    result: num1 - num2
elif operador == "*":
    result == num1 * num2
elif operador == "/":
    result   == num1/num2 

if num2 !=0:
    resultado = num1/num2

#Mostrar o resultado.
print("")
print(f"O resultado da soma é: {soma}" )
print("")
print(f"O resultado da subtração é: {subtracao}" )
print("")
print(f"O resultado da multiplicação é: {multiplicacao}" )
print("")
print(f"O resultado da divisão é: {divisao}" )

