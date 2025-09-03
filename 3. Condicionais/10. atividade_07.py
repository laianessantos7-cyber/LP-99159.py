#Atividade 10- 27/08/2025


#Limpar terminal.
import os
os.system("cls")

#=====BOLETIM=====

nome= input("Digite Seu Nome: ")
idade= float(input("Digite Sua Idade:"))
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media=(nota1+nota2)/2

if media >=9:
    print("Sua nota é A: ")
    print("Aprovado!")
elif media >= 7.5 and media <9:
    print("Sua nota é B: ")
    print("Aprovado!")
elif media >= 6 and media < 7.5:
    print("Sua nota é C: ")    
    print("Aprovado!")
elif media < 4  and media <6:
   print("Sua nota é D: ")
   print("Recuperação.")
else:
    print("Sua nota é E: ")
    print("Recuperação.")

