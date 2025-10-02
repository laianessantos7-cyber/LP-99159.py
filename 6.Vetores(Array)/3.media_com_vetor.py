import os
os.system('cls')

#Crie um programa que leia 3 notas, armazenando em um vetor e calcule a média aritmética. Mostre as 3 notas informadas pelo usuário e informe a média.



# Criando um vetor (lista).
listas_notas=[]


#Constante.
QUANTIDADE_NOTAS=3

#Inserindo notas:

print('Solicitando 3 Notas.')
for i in range(QUANTIDADE_NOTAS):

    nota=float(input(f'Digite a {i+1}ª nota: '))
    listas_notas.append(nota)
    
media=sum(listas_notas) / QUANTIDADE_NOTAS

#Mostrar notas:
print('\nResultado das notas informadas: ')
for i in range(3):
    print(f'Nota:{listas_notas[i]} ')
print('')

print('Resultado da média geral.')
print(f'Média: {media}')

print('FIM')