import os
os.system('cls')

# Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo.


def negativo_positivo(numero):
    
    
    if numero <0:
        
        print(f'Esse número {numero} é negativo.')

    else:
        print(f'Esse número {numero} é positivo.')
    

   
print('Solicitando dados')   
print('')
numero=int(input('Digite um número: '))

negativo_positivo(numero)