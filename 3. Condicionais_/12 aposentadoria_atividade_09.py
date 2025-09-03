#Atividade 12- 28/08/2025 *Feita em casa*


#Limpar terminal.
import os
os.system("cls")


nome= input("Digite Seu Nome: ")
idade= float(input("Digite Sua Idade:"))
matricula_empregado=float(input("Digite sua matricula do empregado: "))
ano_nascimento=float(input("Digite o ano de seu nascimento: "))
tempo_trabalhado= float(input("Digite o tempo de trabalho em anos: "))

print("\n--- Resultado ---")

if idade >= 65 or tempo_trabalhado >= 30:
    print("✅ Requerer aposentadoria.")
else:
    print("❌ Não requerer aposentadoria.")


