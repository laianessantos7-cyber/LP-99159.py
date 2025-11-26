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
print('CREATE - Adicionar / Inserir')
nome='Marta'
lista_cliente.append(nome)
print(f'Nome: {nome} foi inserido com sucesso!')

# READ
print('\nRead - Ler / Mostrar')
print(lista_cliente)

# UPDATE

print('\n Update - Atualizar/ Alterar')
nome_para_atualizar = 'Marta'  
if nome_para_atualizar in lista_cliente:
    novo_nome = 'Marta Silva'
    indice = lista_cliente.index(nome_para_atualizar)
    lista_cliente[indice] = novo_nome
    print(f'O nome {nome_para_atualizar} foi atualizado para {novo_nome}')
else:
    print(f'O nome {nome_para_atualizar} não foi encontrado')
print(lista_cliente)

# DELETE
print('\n Delete - Remover')
nome_para_excluir = ' Maria'

if nome_para_excluir in lista_cliente:
    lista_cliente.remove(nome_para_excluir)
    print(f'{nome_para_excluir} foi excluido com sucesso! ')
else:
    print(f'O nome {nome_para_excluir} não foi encontrado.')

print(lista_cliente)