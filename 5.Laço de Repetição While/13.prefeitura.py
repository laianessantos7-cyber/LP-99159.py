# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados
# sobre o salário e número de filhos das famílias da cidade. A prefeitura deseja saber:  
# a) total de famílias que responderam a pesquisa;
# b) média do salário da população;
# c) média do número de filhos;
# d) maior salário;
# e) menor salário.
# Crie um menu com duas opções.
# Código |   Descrição
#      1 |  Adicionar família
#      2 | Sair e exibir resultados 
# O final da leitura de dados se dará com quando o usuário digitar o número código 2


import os
os.system('cls')

total_familias = 0
soma_salarios = 0.0
soma_filhos = 0
maior_salario = float('-inf')
menor_salario = float('inf')




while True:
    os.system("cls")
    print(""""
Código   |   Descrição
   1     | Adicionar família
   2     | Sair e Exibir resultados    
 
""")

    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            
    
            salario = float(input("Digite o valor salário: "))
            soma_salario += salario

            filhos=float(input('Digite a quantidade de filhos: '))
            media_salarial = soma_salario / total_familias if total_familias != 0 else 0
            if menor_idade == 9999:
                menor_idade = 0
                media_salario = soma_salarios / total_familias
                media_filhos = soma_filhos / total_familias
            print("\n= Exibindo resultados =")
            print(f"Média de salários da população: {media_salarial}")
            print(f"c) Média de filhos: {media_filhos:.2f}")
            input("Pressione enter para continuar...")
        
        case 2:
            print("Saindo do programa.")
            input("Pressione enter para sair...")
            break
        case _:
            print("Opção inválida, tente novamente.")
            input("Pressione enter para continuar...")