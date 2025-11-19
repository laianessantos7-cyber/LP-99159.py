import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float
    cpf: float

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso}')
        print(f'Altura: {self.altura}')
        


lista_de_paciente = []
QUANTIDADE_DE_PACIENTE = 2

# COLETA DOS DADOS
for i in range(QUANTIDADE_DE_PACIENTE):
    paciente = Paciente(
        nome=input('Digite seu nome: '),
        idade=int(input('Digite sua idade: ')),
        peso=float(input('Digite seu peso: ')),
        altura=float(input('Digite sua altura: ')),
        cpf=float(input('Digite seu CPF: '))
    )
    lista_de_paciente.append(paciente)
    print()

nome_do_arquivo = 'dados_pacientes.csv'  

# SALVAR DADOS NO ARQUIVO
with open(nome_do_arquivo, "a", encoding='utf-8') as arquivo_pacientes:
    for paciente in lista_de_paciente:
        arquivo_pacientes.write( f'{paciente.nome},{paciente.idade},{paciente.peso},{paciente.altura},{paciente.cpf}\n')
    print('Dados salvos com sucesso!')

# LER E EXIBIR PACIENTES
print('\nExibindo todos os pacientes: ')
lista = []

try:
    # 'r'- read - leitura
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
        # Recebe todos os dados
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes:
            nome, idade, peso, altura, cpf = paciente.strip().split(',')
            dados_paciente = Paciente(
                nome=nome,
                idade=int(idade),
                peso=float(peso),
                altura=float(altura),
                cpf=float(cpf)
            )
            lista.append(dados_paciente)

        # Exibir todos
        for paciente in lista:
            paciente.exibir_dados()

except FileNotFoundError:
    print('O arquivo não foi encontrado.')
