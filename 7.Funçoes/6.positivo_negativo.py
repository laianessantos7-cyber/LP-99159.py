import os
os.system('cls')



def negativo_positivo(numero):
    
    
    if numero >0:
        
        print(f'Esse número {numero} é positivo.')

    else:
        print(f'Esse número {numero} é negativo.')
    

   
print('Solicitando dados')   
print('')
numero=int(input('Digite um número: '))

negativo_positivo(numero)