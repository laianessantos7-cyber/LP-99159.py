import os
os.system('cls')


# Criando um vetor (lista).
listas_notas=[]

#Inserindo notas:
for i in range(3):

    nota=int(input(f'Digite a {i+1}ª nota: '))
    listas_notas.append(nota)
    
soma=sum(listas_notas)

#Mostrar notas:
for i in range(3):
    print(f'Nota:{listas_notas}[i]')

print(f'Soma: {soma}')

print('FIM')