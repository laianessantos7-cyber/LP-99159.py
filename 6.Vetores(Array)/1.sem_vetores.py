import os
os.system('cls')

soma=0
for i in range(3):

    nota=int(input(f'Digite a {i+1}ª nota: '))
    soma+=nota

print(f'Nota: {nota}')
print(f'Soma: {soma}')
print('FIM')