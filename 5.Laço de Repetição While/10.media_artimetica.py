#Construa um algoritmo que calcule a média aritmética de vários valores inteiros positivos, inseridos pelo usuário. O final da leitura acontecerá quando for lido um valor negativo. Mostre a média aritmética dos números informados pelo usuário.

import os
os.system("cls")

soma=0
contador=0

while True:
      valor=int(input('Digite um valor:  '))
      contador+=1
      if valor< 0:
            contador-=1
            break
      else:
        soma+=valor
      
media = soma / contador
print(f"\nMédia aritmética: {media:.2f}")
    
    