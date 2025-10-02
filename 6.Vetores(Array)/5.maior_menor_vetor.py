import os
os.system('cls')

#Crie um programa que leia 5 números, armazenando em um vetor e informe qual é o menor número e o maior.
#Mostre os números informados pelo usuário.




# Criando um vetor (lista).
listas=[]


#Constante.
QUANTIDADE_NUMEROS=2

#Inserindo notas:
for i in range(5):

    n1=float(input('Digite um número:'))
    listas.append(n1)

menor=min(listas)
maior=max(listas)  
print('')
print('===RESULTADO====')
print('')

for i in range(QUANTIDADE_NUMEROS):
    print(f'Número: {listas[i]}')

print(f'Maior número: {menor}')
print(f"Menor número: {menor}")



print('FIM')




      



