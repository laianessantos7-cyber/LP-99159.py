import os
os.system('cls')

#Crie um programa que leia 6 números, armazenando em um vetor e informe quantos são pares e quantos são ímpares.
# Mostre os números informados pelo usuário.


listas=[]
pares= 0
impares= 0

#Constante.
QUANTIDADE_NUMEROS=6

#Inserindo notas:
print(f'Solicitando {QUANTIDADE_NUMEROS} números')
for i in range(QUANTIDADE_NUMEROS):

    n1=float(input('Digite um número:'))
    
    
    
    if n1 % 2==0:
        pares +=1
    else:
        impares +=1
    listas.append(n1)



print('')


# for i in range(QUANTIDADE_NUMEROS):
#     print(f'\n Números: {listas[i]}')
for n1 in listas:
    print(f'Número: {n1}')
    
    
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")

print('FIM')