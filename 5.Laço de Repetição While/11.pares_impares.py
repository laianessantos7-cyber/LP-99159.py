#Faça um algoritmo que leia uma quantidade não determinada de números inteiros positivos. Calcule: 
#a.quantidade de números pares e ímpares; 
#b.média de valores pares 
#c.média geral dos números lidos. 
#O número que encerrará a leitura será o número zero.

import os
os.system('cls')

pares = 0
impares = 0
soma_pares = 0
soma_total = 0
contador_total = 0


while True:
    numero=int(input('Digite um número inteiro: '))
    if numero==0:
        break

    if numero >0:
        soma_total+=numero
        contador_total+=1
    if numero % 2==0:
        quantidade_pares +=1
        soma_pares+=numero

    else:
        quantidade_impares +=1


media_total = soma_total / contador_total if contador_total !=0 else 0
media_pares = soma_pares / pares if pares !=0 else 0 

#Operaçâo ternária
#media_pares=soma_total/ pares if pares != 0 else 0


print("\n===== RESULTADOS =====")
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Média dos valores pares: {media_pares:.2f}")
print(f"Média geral: {media_total:.2f}")