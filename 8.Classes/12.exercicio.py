import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    nascimento:str
    rg: str
    cpf: str

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Data de Nascimento: {self.nascimento}')
        print(f'RG: {self.rg}')
        print(f'CPF: {self.cpf}')
        


lista_de_usuario = []
QUANTIDADE_DE_USUARIO= 5

# COLETA DOS DADOS
for i in range(QUANTIDADE_DE_USUARIO):
    usuario = Usuario(
        nome=input('Digite seu nome: '),
        nascimento=input('Digite sua data de nascimento: '),
        rg=input('Digite seu RG: '),
        cpf=input('Digite seu CPF: ')
    )
    lista_de_usuario.append(usuario)
    print()

nome_do_arquivo = 'dados_usuario.csv'  

# SALVAR DADOS NO ARQUIVO
with open(nome_do_arquivo, "a", encoding='utf-8') as arquivo_usuario:
    for usuario in lista_de_usuario:
        arquivo_usuario.write( f'{usuario.nome},{usuario.nascimento},{usuario.rg},{usuario.cpf}\n')
print('Dados salvos com sucesso!')

# LER E EXIBIR PACIENTES
print('\nExibindo todos os usuários: ')
lista = []

try:
    # 'r'- read - leitura
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
        # Recebe todos os dados
        lista_todos_usuarios = arquivo.readlines()
        for usuario in lista_todos_usuarios:
            nome, nascimento, rg, cpf=usuario.strip().split(',')
            dados_usuario = Usuario(
                nome=nome,
                nascimento=nascimento,
                rg=rg,
                cpf=cpf
            )
            lista.append(dados_usuario)

        # Exibir todos
        for usuario in lista:
            usuario.exibir_dados()

except FileNotFoundError:
    print('O arquivo não foi encontrado.')
