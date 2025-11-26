import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    admissao: str
    matricula: str
    endereco: str

    def funcionario_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Data de Admissão: {self.admissao}')
        print(f'Matricula: {self.matricula}')
        print(f'Endereço: {self.endereco}')
        print()

@dataclass
class Cliente:
    nome: str
    nascimento: str
    endereco: str
    
    def cliente_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Data de Nascimento: {self.nascimento}')
        print(f'Endereço: {self.endereco}')
        print()

lista_de_funcionario = []
lista_de_cliente = []

QUANTIDADE_DE_FUNCIONARIO = 3
QUANTIDADE_DE_CLIENTE = 3

# COLETA DOS FUNCIONÁRIOS
for funcionario in range(QUANTIDADE_DE_FUNCIONARIO):
    print('= DADOS DE FUNCIONÁRIOS = ')
    funcionario = Funcionario(
        nome=input('Digite seu nome: '),
        admissao=input('Digite sua data de admissão: '),
        matricula=input('Digite sua Matricula: '),
        endereco=input('Digite seu Endereço: ')
    )
    lista_de_funcionario.append(funcionario)


# COLETA DOS CLIENTES
for cliente in range(QUANTIDADE_DE_CLIENTE):
    print('= DADOS DE CLIENTES = ')
    cliente = Cliente(
        nome=input('Digite seu nome: '),
        nascimento=input('Digite sua data de nascimento: '),
        endereco=input('Digite seu Endereço: ')
    )
    lista_de_cliente.append(cliente)


# SALVAR FUNCIONÁRIOS
nome_do_arquivo = 'dados_funcionario.csv'
with open(nome_do_arquivo, "a", encoding='utf-8') as arquivo_funcionario:
    for funcionario in lista_de_funcionario:
        arquivo_funcionario.write(
            f'{funcionario.nome},{funcionario.admissao},{funcionario.matricula},{funcionario.endereco}\n'
        )
    print('Dados salvos com sucesso!')

# SALVAR CLIENTES
nome_arquivo = 'dados_clientes.csv'
with open(nome_arquivo, "a", encoding='utf-8') as arquivo_cliente:
    for cliente in lista_de_cliente:
        arquivo_cliente.write(
            f'{cliente.nome},{cliente.nascimento},{cliente.endereco}\n'
        )
    print('Dados salvos com sucesso!')

print('\n= EXIBINDO TODOS OS DADOS = ')

lista_todos_funcionarios = []

# LEITURA FUNCIONÁRIOS
try:
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
        funcionario = arquivo.readlines()

        for cliente in funcionario:
            linha = cliente.strip().split(',')

            try:
                nome, admissao, matricula, endereco = linha
                funcionario = Funcionario(nome, admissao, matricula, endereco)
                lista_todos_funcionarios.append(funcionario)

            except ValueError:
                pass

except FileNotFoundError:
    print('O arquivo não foi encontrado.')

# EXIBIR FUNCIONÁRIOS
for funcionario in lista_todos_funcionarios:
    funcionario.funcionario_dados()

lista_todos_clientes = []

# LEITURA CLIENTES
try:
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
        cliente = arquivo.readlines()

        for funcionario in cliente:
            linha2 = funcionario.strip().split(',')

            try:
                nome, nascimento, endereco = endereco
                cliente = Cliente(nome, nascimento, endereco)
                lista_todos_clientes.append(cliente)

            except ValueError:
                pass

except FileNotFoundError:
    print('O arquivo não foi encontrado.')

# EXIBIR CLIENTES
for cliente in lista_todos_clientes:
    cliente.cliente_dados()
