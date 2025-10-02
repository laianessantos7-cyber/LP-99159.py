import os
os.system('cls')

#Crie um algoritmo que preencha um vetor com 5 números, mostre a quantidade de números negativos e a soma dos números positivos desse vetor.


numeros=[]
soma_positivos=0
quantidade_negativo=0

#Constante.


#Inserindo notas:

for i in range(5):

    numero=int(input(f'Digite um número:'))
    numeros.append(numero)

if numero >0:
    soma_positivos+= numero
elif numero <0:
        quantidade_negativo +=1

print('\n =RESULTADO =')
print(f"Quantidade de números negativos: {quantidade_negativo}")
print(f'Soma dos positivos {soma_positivos}')
    

print('FIM')