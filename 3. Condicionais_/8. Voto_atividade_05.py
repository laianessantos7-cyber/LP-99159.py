#Atividade 05- 27/08/2025


#Limpar terminal.
import os
os.system("cls")

idade= int(input("Digite sua idade: "))

if idade < 16:
    print("Você não pode votar!")

elif idade > 16 and idade < 17:
    print("Voto Opcional.")

elif idade >=18 and idade < 65:
    print("Voto obrigatório!")

else:
    print("Não são obrigados a votar.")


