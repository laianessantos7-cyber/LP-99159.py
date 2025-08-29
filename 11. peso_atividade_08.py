#Atividade 08- 28/08/2025 *Feita em casa*


#Limpar terminal.
import os
os.system("cls")



nome= input("Digite Seu Nome: ")
idade= float(input("Digite Sua Idade:"))
peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
media=(peso+altura)

if media <= 18.5:
    print("Abaixo do Peso. ")
    
elif media >= 18.6 and media < 24.9:
    print("Peso ideal! ")
    print("Parabéns!")
elif media >= 25.0 and media < 29.9:
    print("Levemente acima do peso. ")    

elif media >= 30.0 and media < 34.9:
   print("Obesidade grau I. ")

elif media >= 35.0 and media <39.9:
   print("Obesidade grau II (severa). ")

else:
   print("Obesidade III (mórbida). ")
