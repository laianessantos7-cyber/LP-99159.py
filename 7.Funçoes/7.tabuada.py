import os
os.system('cls')


def tabuada(numero, operador):
    for i in range(1,11):
        print(f'{numero} x {i} = {numero * i }')




numero=int(input('Digite um número: '))

os.system('cls')
tabuada(numero)

print('==FIM==')