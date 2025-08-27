
#Atividade 03- 22/08/2025

#Limpar terminal.
import os
os.system("cls")


n1=float(input("Digite a primeira nota: "))
print("")
n2=float(input("Digite a segunda nota: "))
media=(n1+n2)/2

if media >=7:
    resultado= "Aprovado!"

else:
    resultado="Reprovado!"
print("")    
print(f"Média: {media}")
print("")
print(f"Resultado: {resultado}")



