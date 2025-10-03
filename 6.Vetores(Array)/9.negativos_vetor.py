import os
os.system('cls')

# Crie um algoritmo que receba do usuário valores e armazene em um vetor 5 números, caso seja informado um valor negativo, atribua o valor 0.
# - Liste os valores do vetor.

#Variaveis.

lista_numeros=[] #- Lista.


#Constante.QUANTIDADE_NUMEROS=5

#Inserindo notas:
print(f'Solicitando números:')

for i in range(5):
    numero = int(input('Digite um número: '))
    
    
    if numero < 0:
        numero=0
        lista_numeros.append(numero)
    

print('\nExibindo numeros. ')
for i, numero in enumerate(lista_numeros, start=1):
    print(f'{i}º número: {numero}')

print("FIM")

