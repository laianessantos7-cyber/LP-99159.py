import os
os.system('cls')

#Crie um programa que leia 4 notas, armazenando em um vetor e calcule a média aritmética.
# Verifique a situação do aluno considerando:
# 	- Média maior ou igual a 7: Aprovado.
# 	- Média maior ou igual a 5: Recuperação.
# 	- Média menor que 5: Reprovado.
# Mostre as 4 notas informadas pelo usuário e informe a média.



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




      



