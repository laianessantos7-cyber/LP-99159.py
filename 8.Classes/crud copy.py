import os 
os.system('cls || clear')

# CRUD usando lista.
# Create = criar / salvar
# Read = buscar / selecionar
# Update = atualizar / modificar
# Delete = excluir

# Criando uma lista

lista_cliente = []

# CREATE
print("===== ABA DO CLIENTE====")


print("""
Código \t
1 \t Adicionar
2 \t Atualizar
3 \t Excluir


""")

codigo= input("Digite o código: ")

match codigo:
    case "1":
        print('CREATE - Adicionar / Inserir')
        nome=input('Digite o nome: ')
        lista_cliente.append(nome)
        print(f'Nome: {nome} foi inserido com sucesso!')

# READ
        print('\nRead - Ler / Mostrar')
        print(lista_cliente)
    case "2":
        # UPDATE
        print('\n Update - Atualizar/ Alterar')
        nome_para_atualizar=input('Digite o nome para qual deseja atualizar: ') 
        if nome_para_atualizar in lista_cliente:
                     novo_nome = nome_para_atualizar
        indice = lista_cliente.index(nome_para_atualizar)
        lista_cliente[indice] = novo_nome
        print(f'O nome {nome_para_atualizar} foi atualizado para {novo_nome}')
        else:
            print(f'O nome {nome_para_atualizar} não foi encontrado')
             print(lista_cliente)  
           
           
    case "3":

        print("Excluir: ")
   
    case _: 
        print("Ação indisponível! ")
    






# DELETE
print('\n Delete - Remover')
nome_para_excluir=input('Informe qual nome deseja excluir: ')

if nome_para_excluir in lista_cliente:
    lista_cliente.remove(nome_para_excluir)
    print(f'{nome_para_excluir} foi excluido com sucesso! ')
else:
    print(f'O nome {nome_para_excluir} não foi encontrado.')

print(lista_cliente)