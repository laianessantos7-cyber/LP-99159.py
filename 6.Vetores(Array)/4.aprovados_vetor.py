import os
os.system('cls')


# Criando um vetor (lista).
listas_notas=[]


#Constante.
QUANTIDADE_NOTAS=4

#Inserindo notas:
for i in range(QUANTIDADE_NOTAS):

    nota=int(input(f'Digite a {i+1}ª nota: '))
    listas_notas.append(nota)
    
media=sum(listas_notas) / QUANTIDADE_NOTAS


#Mostrar notas:
print("====BOLETIM====")
for i in range(3):
    print(f'Nota:{listas_notas[i]} ')

print(f'Média: {media}')


if media >= 7:
    print("Aprovado!")
elif media >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")



print('FIM')




      



