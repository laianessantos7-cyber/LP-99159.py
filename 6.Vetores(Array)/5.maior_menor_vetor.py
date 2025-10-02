import os
os.system('cls')

#Crie um programa que leia 5 números, armazenando em um vetor e informe qual é o menor número e o maior.
#Mostre os números informados pelo usuário.




# Criando um vetor (lista).
listas=[]


#Constante.

#Inserindo notas:
for i in range(5):

    n1=int(input(f'Digite o {i+1}ª número : '))
    listas.append(n1)
    
print('')
print('===RESULTADO====')
print('')
for i in range(1):
    
    print(f'Maior: {max(listas)}')
    print(f"Menor: {min(listas)}")



print('FIM')




      



