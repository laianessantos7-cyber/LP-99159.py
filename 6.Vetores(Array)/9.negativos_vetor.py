import os
os.system('cls')

# Crie um algoritmo que receba do usuário valores e armazene em um vetor 5 números, caso seja informado um valor negativo, atribua o valor 0.
# - Liste os valores do vetor.


listas=[]
negativos= 0
positivos= 0
soma=0  

#Constante.
QUANTIDADE_NUMEROS=5

#Inserindo notas:
print(f'Solicitando {QUANTIDADE_NUMEROS} números')
for i in range(QUANTIDADE_NUMEROS):

    numero=int(input(f'Digite o {i+1}ª número:'))
    listas.append(numero)

print('')
for n1 in listas:
    if i <0:
        negativos+=1
    else:
        positivos.append(negativos)

    
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f'Soma dos positivos {sum(positivos)}')
    

print('FIM')