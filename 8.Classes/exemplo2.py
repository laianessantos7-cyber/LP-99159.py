import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    telefone: str

QUANTIDADE_ALUNOS= 2
lista_alunos=[]

print('Solicitando dados do aluno')
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome=input('Nome: '),
        idade=int(input('Idade: ')),
        email=input('E-mail: '),
        telefone=input('Telefone: ')
    )
    lista_alunos.append(aluno)

print()
print('Salvando dados')
arquivo='dados_alunos.txt'

with open(arquivo, 'a') as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f'\n{aluno.nome}, \n{aluno.idade} , \n{aluno.email}, \n{aluno.telefone}')

print('Salvo com sucesso! ')