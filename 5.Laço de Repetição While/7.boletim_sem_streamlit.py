import os
os.system('cls')

#Escreva um algoritmo que leia três notas de um aluno. Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
#Após receber as notas dentro dos parâmetros acima, calcule a média e verifique se o aluno está aprovado, recuperação ou reprovado considerando os seguintes critérios: 
#Se a média for a partir de 7, aprovado. Se a média for entre 5 e 6,9, o aluno está em recuperação; Caso seja menor que 5, o aluno está reprovado.


print("====BOLETIM====")
      
notas=[]


for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Digite a nota {i} (0 a 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break  #
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Inválido! Digite um número.")


media = sum(notas) / len(notas)
print(f"\nMédia do aluno: {media:.2f}")


if media >= 7:
    print("Aluno aprovado!")
elif 5 <= media < 7:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")