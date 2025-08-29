#Atividade 10- 29/08/2025


#Limpar terminal.
import os
os.system("cls")
idade= int(input("Digite sua idade: "))


if idade >=18 and idade < 65:
    print("Voto obrigatório!")

else:
    print("Não são obrigados a votar.")
