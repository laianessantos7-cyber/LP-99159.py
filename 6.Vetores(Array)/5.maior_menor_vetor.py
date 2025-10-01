import os
os.system('cls')


# Criando um vetor (lista).
listas_num=[]


#Constante.

#Inserindo notas:
for i in range(5):

    n1=int(input(f'Digite o {i+1}ª número : '))
    listas_num.append(n1)
    

print('===RESULTADO====')
for i in range(5):
    
    print(f'Maior: {max(listas_num)}')
    print(f"Menor: {min(listas_num)}")



print('FIM')




      



