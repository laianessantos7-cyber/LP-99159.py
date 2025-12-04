import os
import time
from dataclasses import dataclass
os.system('cls || clear ') #Limpar terminal


lista_cliente=[]
lista_produto=[]

@dataclass
class Endereço:
    logradouro: str
    numero: str
    cidade: str
    estado: str

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
   
@dataclass
class Produto:
    nome: str
    quantidade: str
    lote: str
    validade: str
    

    def mostrar_dados(self):
        print('====== CLIENTE ======')
        print(f'\n Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Telefone: {self.telefone}')
        print('====== ENDEREÇO ======')
        print(f'Logradouro: {self.endereco.logradouro}')
        print(f'Número: {self.endereco.numero}')
        print(f'Cidade: {self.endereco.cidade}')
        print(f'Estado: {self.endereco.estado}')
        print('====== PRODUTO ======')
        print(f'Nome: {self.nome}')
        print(f'Número: {self.quantidade}')
        print(f'Cidade: {self.lote}')
        print(f'Estado: {self.validade}')

def lista_vazia(lista_cliente):
    if not lista_cliente:
        print('\nNão há clientes cadastrados')
        return True
    return False

def lista_vazia(lista_produto):
    if not lista_produto:
        print('\nNão há produtos cadastrados')
        return True
    return False

def adicionar_cliente(lista_cliente):
    print('\n--------- Adicionar novo Cliente ---------')
    nome=input('Nome: ')
    email=input('E-mail: ')
    telefone=input('Telefone: ')
    endereco=Endereço(
        logradouro=input('Logradouro: '),
        numero=input('Número: '),
        cidade=input('Cidade: '),
        estado=input('Estado: ')
    )

    novo_cliente=Cliente(
        nome=nome,
        email=email,
        telefone=telefone,
        endereco=endereco
    )

    lista_cliente.append(novo_cliente)
    print(f'\nCliente {nome} adicionado com sucesso!')

def adicionar_produto(lista_produto):
    print('\n--------- Adicionar novo Produto ---------')
    nome=input('Nome: ')
    quantidade=input('Quantidade: ')
    lote=input('Lote: ')
    validade=input('Validade: ')

    novo_produto=Produto(
        nome=nome,
        quantidade=quantidade,
        lote=lote,
        validade=validade
    )

    lista_produto.append(novo_produto)
    print(f'\nProduto {nome} adicionado com sucesso!')

def encontrar_por_nome_cliente(lista_cliente, nome_buscar):
    for cliente in lista_cliente:
        if cliente.nome.lower() == nome_buscar.lower():
            return cliente
    return None

def encontrar_produto_lote(lista_produto, lote_buscar):
    for produto in lista_produto:
        if produto.lote.lower() == lote_buscar.lower():
            return produto
    return None

def mostrar_todos_clientes(lista_cliente):
    if lista_vazia(lista_cliente):
        return
    print('\n---- Lista de Clientes -----')
    for cliente in lista_cliente:
     cliente.mostrar_dados()

def mostrar_todos_produtos(lista_produto):
    if lista_vazia(lista_produto):
        return
    print('\n---- Lista de Produtos -----')
    for produto in lista_produto:
     produto.mostrar_dados()


def atualizar_clientes(lista_cliente):
    if lista_vazia(lista_cliente):
        return
    mostrar_todos_clientes(lista_cliente)
    
    print('\n----- Atualizar dados do Cliente -----')
    nome_buscar = input('Digite o Nome Completo do Cliente: ')
    cliente = encontrar_por_nome_cliente(lista_cliente, nome_buscar)

    if cliente:
        print('\nCliente encontrado. Deixe em branco para manter o valor atual!\n')

        print(f'Nome: {cliente.nome}')
        novo_nome=input('Nome Atualizado.')
         
        print(f'E-mail: {cliente.email}')
        novo_email=input('E-mail Atualizado: ')
        
        print(f'Telefone: {cliente.telefone}')
        novo_telefone=input('Telefone Atualizado: ')

        print(f'Endereço: {cliente.endereco}')
        novo_endereco=input('Endereço Atualizado: ')

        if novo_nome:
             cliente.nome=novo_nome
        if novo_email:
            cliente.email=novo_email
        if novo_telefone:
                cliente.telefone=novo_telefone
        if novo_endereco:
                cliente.endereco=novo_endereco
        
        print('\nDados atualizados com sucesso!')

    else:
        print(f'\nNome {nome_buscar} não encontrado!')

def atualizar_produto(lista_produto):
    if lista_vazia(lista_produto):
        return
    mostrar_todos_produtos(lista_produto)
    
    print('\n----- Atualizar dados dos Produtos -----')
    lote_buscar = input('Digite o Lote do Produto: ')
    produto = encontrar_produto_lote(lista_produto, lote_buscar)

    if produto:
        print('\nProduto encontrado. Deixe em branco para manter o valor atual!\n')

        print(f'Nome: {produto.nome}')
        novo_nome_produto=input('Nome Atualizado.')
         
        print(f'Quantidade: {produto.quantidade}')
        nova_quantidade=input('Quantidade Atualizada: ')
        
        print(f'Lote: {produto.lote}')
        novo_lote=input('Lote Atualizado: ')

        print(f'Validade: {produto.validade}')
        nova_validade=input('Validade Atualizada: ')
        
        if novo_nome_produto:
             produto.nome=novo_nome_produto
        if nova_quantidade:
            produto.quantidade=nova_quantidade
        if nova_validade:
                produto.validade=nova_validade
        
        print('\nDados atualizados com sucesso!')

    else:
        print(f'\nLote {lote_buscar} não encontrado!')

def excluir_cliente(lista_cliente):
    if lista_vazia(lista_cliente):
        return
    mostrar_todos_clientes(lista_cliente)
    nome_buscar=input('\nDigite o Nome Completo do Cliente que deseja excluir.')
    cliente=nome_buscar(lista_cliente,nome_buscar)
    if cliente:
        lista_cliente.remove(cliente)
        print(f'\nCliente{cliente.nome} excluido com sucesso!')

def excluir_produto(lista_produto):
    if lista_vazia(lista_produto):
        return
    mostrar_todos_produtos(lista_produto)
    lote_buscar=input('\nDigite o lote do produto que deseja excluir')
    produto=lote_buscar(lista_produto,lote_buscar)
    if produto:
        lista_produto.remove(produto)
        print(f'\nProduto{produto.lote} excluido com sucesso!')





while True:
    print("""
          
         Empresa Mamão com Acúçar
------------ Área do Cliente ------------
    1- Adicionar Cliente
    2- Adicionar Produto
    3- Mostrar todos os clientes
    4- Mostrar todos os produtos
    5- Atualizar Cliente
    6- Atualizar Produto
    7- Excluir Produto
    8- Excluir Cliente   
    0- Sair
""")
    try:
        opcao=int(input('Digite opção desejada: '))
    except ValueError:
        print('\nEntrada inválida. Digite um número.')
        time.sleep(2)
        os.system('cls || clear')
        continue

    match opcao:
        case 1:
            adicionar_cliente(lista_cliente)
        case 2:
            adicionar_produto(lista_produto)
        case 3:
            mostrar_todos_clientes(lista_cliente)
        case 4:
            mostrar_todos_produtos(lista_produto)
        case 5:
            atualizar_clientes(lista_cliente)
        case 6:
            atualizar_produto(lista_produto)
        case 7:
            excluir_cliente(lista_cliente)
        case 8:
            excluir_produto(lista_produto)
        case 0:
            print('\nSaindo do programa...')
            break
        case _:
            print('\nOpção inválida!')

    if opcao != 0:
        time.sleep(2)
