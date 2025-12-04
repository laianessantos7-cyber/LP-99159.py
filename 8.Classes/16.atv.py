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

@dataclass
class Aluno:
    nome: str
    nascimento: str
    r_a: str
    curso: str
    endereco: Endereço

    def mostrar_dados(self):
        print(f'\nNome: {self.nome}')
        print(f'Data de Nascimento: {self.nascimento}')
        print(f'R.A: {self.r_a}')
        print(f'Curso: {self.curso}')
        print('====== ENDEREÇO ======')
        print(f'Logradouro: {self.endereco.logradouro}')
        print(f'Número: {self.endereco.numero}')
        print(f'Cidade: {self.endereco.cidade}')
        print(f'Estado: {self.endereco.estado}')


def lista_vazia(lista_alunos):
    if not lista_alunos:
        print('\nNão há alunos cadastrados')
        return True
    return False


def adicionar_alunos(lista_alunos):
    print('\n--------- Adicionar novo Aluno ---------')
    nome=input('Nome: ')
    nascimento=input('Data de Nascimento: ')
    r_a=input('R.A: ')
    curso=input('Curso: ')
    endereco=Endereço(
        logradouro=input('Logradouro: '),
        numero=input('Número: '),
        cidade=input('Cidade: '),
        estado=input('Estado: ')
    )

    novo_aluno=Aluno(
        nome=nome,
        nascimento=nascimento,
        r_a=r_a,
        curso=curso,
        endereco=endereco
    )

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


def atualizar_alunos(lista_alunos):
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

        print(f'Nascimento atual: {aluno.nascimento}')
        novo_nascimento=input('Nova Data de Nascimento: ')

        print(f'R.A atual: {aluno.r_a}')
        novo_r_a=input('Novo R.A: ')

        print(f'Curso atual: {aluno.curso}')
        novo_curso=input('Novo Curso: ')

        print(f'Logradouro atual: {aluno.endereco.logradouro}')
        novo_logradouro=input('Novo Logradouro: ')

        print(f'Número atual: {aluno.endereco.numero}')
        novo_numero=input('Novo Número: ')

        print(f'Cidade atual: {aluno.endereco.cidade}')
        nova_cidade=input('Nova Cidade: ')

        print(f'Estadotual: {aluno.endereco.estado}')
        novo_estado=input('Novo Estado: ')

        if novo_nome:
            aluno.nome=novo_nome
        if novo_nascimento:
            aluno.nascimento=novo_nascimento
        if novo_r_a:
            aluno.r_a=novo_r_a
        if novo_curso:
            aluno.curso=novo_curso
        if novo_logradouro:
            aluno.endereco.logradouro=novo_logradouro
        if novo_numero:
            aluno.endereco.numero=novo_numero
        if nova_cidade:
            aluno.endereco.cidade=nova_cidade
        if novo_estado:
            aluno.endereco.estado=novo_estado

        print('\nDados atualizados com sucesso!')

    else:
        print(f'\nR.A {r_a_buscar} não encontrado!')


def excluir_aluno(lista_alunos):
    if lista_vazia(lista_alunos):
        return
    
    mostrar_todos_alunos(lista_alunos)
    r_a_buscar=input('\nDigite O R.A do aluno que deseja excluir: ')
    aluno=encontrar_por_r_a(lista_alunos,r_a_buscar)

    if aluno:
        lista_alunos.remove(aluno)
        print(f'\nAluno {aluno.nome} excluído com sucesso!')
    else:
        print('\nAluno não encontrado.')


# Menu
while True:
    print("""
------------ Portal do Aluno ------------
    1- Adicionar
    2- Mostrar todos
    3- Atualizar
    4- Excluir
    0- Sair
""")
        
    try:
        opcao = int(input('Digite uma opção: '))
    except ValueError:
        print('\nEntrada inválida. Digite um número.')
        time.sleep(2)
        os.system('cls || clear')
        continue

    match opcao:
        case 1:
            adicionar_alunos(lista_alunos)
        case 2:
            mostrar_todos_alunos(lista_alunos)
        case 3:
            atualizar_alunos(lista_alunos)
        case 4:
            excluir_aluno(lista_alunos)
        case 0:
            print('\nSaindo do programa...')
            break
        case _:
            print('\nOpção inválida!')

    if opcao != 0:
        time.sleep(2)
