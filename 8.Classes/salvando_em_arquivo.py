import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: str


def exibir_dados(self):
    print(f'Nome: {self.nome} \n Idade: {self.idade}')


lista_de_paciente=[]
QUANTIDADE_DE_PACIENTE=2

for i in range (QUANTIDADE_DE_PACIENTE):
    paciente=Paciente(
        nome=input('Digite seu nome: '),
        idade=input('Digite sua idade:'),
    )
    lista_de_paciente.append(paciente)
    print()

nome_do_arquivo=' dados_pacientes.csv'
with open (nome_do_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_de_paciente:
        arquivo_pacientes.write(f'\n{paciente.nome}, \n{paciente.idade}')
        print('Dados salvos com sucesso.')


        print('\nExibindo lista de pacientes: ')
        for paciente in lista_de_paciente:
             paciente.exibir_dados()