<<<<<<< HEAD
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
    cidade=input('Cidade: ')
    estado=input('Estado: ')
    
    novo_aluno=Aluno(nome,nascimento,r_a,curso,endereco,logradouro, numero, cidade,estado)
    lista_alunos.append(novo_aluno)
    
    print(f'\nAluno(a) {nome} adicionado com sucesso!')


def encontrar_por_r_a(lista_alunos, r_a_buscar):
    for aluno in lista_alunos:
        if aluno.r_a.lower() == r_a_buscar.lower():
            return aluno
    return None

def mostrar_todos_alunos(lista_alunos):
    if lista_vazia(lista_alunos):
        return
    
    print('\n---- Lista de Alunos ----')
    for aluno in lista_alunos:
        aluno.mostrar_dados()

def atualizar_aluno(lista_alunos):
    if lista_vazia(lista_alunos):
        return
    mostrar_todos_alunos(lista_alunos)

    print('\n----- Atualizar dados do aluno -----')
    r_a_buscar = input('Digite o R.A do Aluno: ')
    aluno = encontrar_por_r_a(lista_alunos, r_a_buscar)

    if aluno:
        print('\nAluno encontrado. Deixe em branco para manter o valor atual.\n')

        print(f'Nome atual: {aluno.nome}')
        novo_nome=input('Novo Nome: ')
         
        print(f'Nascimento Atual: {aluno.nascimento}')
        novo_nascimento=input('Data de Nascimento: ')

        print(f'R.A Atual: {aluno.r_a}')
        novo_r_a=input('R.A Atual: ')

        print(f'Curso Atual: {aluno.curso}')
        novo_curso=input('Curso Atual: ')

        print(f'Endereço: {aluno.endereco}')
        novo_endereco=input('Endereço Atual: ')

        print(f'Logradouro: {aluno.logradouro}')
        novo_logradouro=input('Logradouro Atual: ')

        print(f'Número: {aluno.numero}')
        novo_numero=input('Número Atual: ')
        
        print(f'Cidade: {aluno.cidade}')
        nova_cidade=input('Cidade Atual: ')

        print(f'Estado: {aluno.estado}')
        novo_estado=input('Estado Atual: ')

        if novo_nome:
            aluno.nome=novo_nome
        if novo_nascimento:
            aluno.nascimento=novo_nascimento
        if novo_r_a:
            aluno.r_a=novo_r_a
        if novo_curso:
            aluno.curso=novo_curso
        if novo_endereco:
            aluno.endereco=novo_endereco
        if novo_logradouro:
            aluno.logradouro=novo_logradouro
        if novo_numero:
            aluno.numero=novo_numero
        if nova_cidade:
            aluno.cidade=nova_cidade
        if novo_estado:
            aluno.estado=novo_estado

        print('\nDados atualizados com sucesso!')

    else:
        print(f'\nR.A{r_a_buscar} não encontrado!')

def excluir_aluno(lista_alunos):
    if lista_vazia(lista_alunos):
        return
    
    mostrar_todos_alunos(lista_alunos)
    r_a_buscar=input('\nDigite O R.A do aluno que deseja excluir')
    aluno=encontrar_por_r_a(lista_alunos,r_a_buscar)

    if aluno:
        lista_alunos.remove(aluno)
        print(f'\nAluno{aluno.nome} excluido com sucesso!')
    else:
        print()
=======
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
>>>>>>> c2cf3165e264c22a6b610161254f95a3aa5c5d03
