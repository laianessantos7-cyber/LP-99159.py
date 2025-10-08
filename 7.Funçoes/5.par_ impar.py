import os
os.system('cls')


#Crie uma função  que receba um número e mostre uma
#Mensagem informando se o número é par ou ímpar.



def par_impar(numero):
    
    
    if numero % 2==0:
        print(f'Esse número {numero} é par.')
        
    else:
        print(f'Esse número {numero} é impar.')

   
print('Solicitando dados')   
print('')
numero=int(input('Digite um número: '))

par_impar(numero)