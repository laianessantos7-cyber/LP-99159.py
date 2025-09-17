import os
os.system('cls')

#Escreva um algoritmo que leia três notas de um aluno. Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
#Após receber as notas dentro dos parâmetros acima, calcule a média e verifique se o aluno está aprovado, recuperação ou reprovado considerando os seguintes critérios: 
#Se a média for a partir de 7, aprovado. Se a média for entre 5 e 6,9, o aluno está em recuperação; Caso seja menor que 5, o aluno está reprovado.


print("====BOLETIM====")

QUANTIDADE_NOTAS=3
soma=n1+n2
media = soma / QUANTIDADE_NOTAS

n1 = float(input(f"Digite sua primeira nota: "))
n2 = float(input(f"Digite sua segunda nota: "))



if n1 < 0 or n2 > 10:


            print("Mostrar Resultado.")
if media >=7:
            print("Aprovado!")
            print(f"Média: {media}")
            
        elif media >= 5 or media >6 or media >9:
              print("Recuperação")
              
        elif media <5:
              print(f"Média{media}")
              print("Reprovado")

      
     



