#Foi feita uma pesquisa entre os habitantes de uma região.  Foram coletados os dados de idade, sexo (M/F) e salário. 
#Faça um algoritmo que informe:  
# a) a média de salário do grupo;
# b) maior e menor idade do grupo;
# c) quantidade de mulheres com salário a partir de R$ 5.000,00.
#Crie um menu com três opções.
#Código |   Descrição
#        1        |   Adicionar pessoa

#       2       |   Exibir resultados

#       3       |   Sair
#O final da leitura de dados se dará com quando o usuário digitar o número código 3. 
#Ao adicionar uma pessoa, deve-se limpar o terminal e apresentar o menu novamente.

import os
os.system('cls')


menor_idade = 9999
maior_idade = 0
soma_salario = 0
quantidade_salarios = 0
mulheres5k = 0

while True:
    os.system("cls")
    print(""""
Código   |   Descrição
   1     | Adicionar pessoa
   2     | Exibir resultados    
   3     | Sair
""")

    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            
            idade = int(input("Digite idade: "))
            sexo = input("Digite o sexo (M/F)").upper()
            salario = float(input("Digite o valor salário: "))

            
            quantidade_salarios += 1
            soma_salario += salario

            
            if idade < menor_idade:
                menor_idade = idade

            if idade > maior_idade:
                maior_idade = idade

           
            if salario >= 5000 and sexo == "F":
                mulheres5k += 1

        case 2:
            media_salarial = soma_salario / quantidade_salarios if quantidade_salarios != 0 else 0
            if menor_idade == 9999:
                menor_idade = 0
               
            print("\n= Exibindo resultados =")
            print(f"Média de salários do grupo: {media_salarial}")
            print(f"Menor idade do grupo: {menor_idade}")
            print(f"Maior idade do grupo: {maior_idade}")
            print(f"Quantidade de mulheres com salário acima de 5 mil: {mulheres5k}")
            input("Pressione enter para continuar...")
        case 3:
            print("Saindo do programa.")
            input("Pressione enter para sair...")
            break
        case _:
            print("Opção inválida, tente novamente.")
            input("Pressione enter para continuar...")