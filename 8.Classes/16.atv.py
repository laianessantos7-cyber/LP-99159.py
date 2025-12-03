import os
import time
from dataclasses import dataclass

os.system('cls || clear ') # Limpar terminal

lista_alunos=[]
@dataclass

class Endereço:
    logradouro: str
    numero: str
    cidade: str
    estado: str

class Aluno:
    nome: str
    nascimento: str
    r_a: str
    curso: str
    endereco: str

def mostrar_dados(self):
    print(f'\nNome:{self.nome}')
    print(f'Data de Nascimento: {self.nascimento}')
    print(f'R.A: {self.r_a}')
    print(f'Curso: {self.curso}')
    print('= ENDEREÇO = \n')
    print(f'Endereço: {self.endereco}')
    print(f'Logradouro: {self.endereco.logradouro}')
    print(f'Número: {self.endereco.numero}')
    print(f'Cidade: {self.endereco.cidade}')
    print(f'Estado: {self.endereco.estado}')

def lista_vazia(lista_alunos):
    if not lista_alunos:
        print('\nNão há alunos cadastrados')
        return True
    return False



def adicionar_aluno(lista_alunos):
    print('\n--------- Adicionar novo Aluno ---------')
    nome=input('Nome: ')
    nascimento=input('Data de Nascimento: ')
    r_a=input('R.A: ')
    curso=input('Curso: ')
    endereco=input('Endereço: ')
    logradouro=input('Logradouro: ')
    numero=input('Número:')