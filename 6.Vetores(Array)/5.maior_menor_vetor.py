import os
os.system('cls')

#Crie um programa que leia 5 números, armazenando em um vetor e informe qual é o menor número e o maior.
#Mostre os números informados pelo usuário.




# Criando um vetor (lista)
numeros = []



# Lendo os números
for i in range(5):
    n = float(input(f'Digite o {i+1}º número: '))
    numeros.append(n)

# Encontrando o menor e o maior número
menor = min(numeros)
maior = max(numeros)

# os resultados
print('\n=== RESULTADO ===\n')
print('Números informados:')
for num in numeros:
    print(f'Número: {num}')

print(f'\nMaior número: {maior}')
print(f'Menor número: {menor}')

print('\nFIM')
      



