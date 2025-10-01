import os
os.system('cls')


# Criando um vetor (lista).
listas_notas=[]


#Constante.
QUANTIDADE_NOTAS=3

#Inserindo notas:
for i in range(QUANTIDADE_NOTAS):

    nota=int(input(f'Digite a {i+1}ª nota: '))
    listas_notas.append(nota)
    
media=sum(listas_notas) / QUANTIDADE_NOTAS

#Mostrar notas:
print('\nResultado: ')
for i in range(3):
    print(f'Nota:{listas_notas[i]} ')

print(f'Média: {media}')

print('FIM')