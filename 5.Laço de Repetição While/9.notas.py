#Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota, se a resposta do usuário for “N”, o programa fará a média aritmética das notas informadas e mostrará a média aritmética para o usuário.
#Obs.: Use um contador dentro do laço de repetição para contar a quantidade de iterações (loops).

import os
os.system("cls")

soma=0.0
contador=0

while True:
      nota=float(input('Digite uma nota:  '))
      
      soma+=nota
      contador+=1

      resp=input('Deseja inserir mais uma nota? (S/N):').upper()
      if resp== 'N':
            break
      media=soma/contador
    
    
print(f"Média aritmética: {media:.2f}")
print(f"Foram inseridas {contador} notas.")