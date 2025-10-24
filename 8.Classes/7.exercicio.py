import os
os.system("cls")

from dataclasses import dataclass

# Criando Classe
@dataclass
class Pessoas:
    nome: str
    cpf: str
    telefone: float

    def mostrar_dados(self):
        print(f'Nome: {self.nome} \n' )
        print(f'CPF: {self.cpf} \n')
        print(f'Telefone: {self.telefone} \n')
   
   
    def dados_sms_marketing(self):
        print(f'Telefone: {self.telefone} \n')


lista_de_pessoas=[]

for i in range(3):
    dados_cliente= Pessoas(nome=input('Digite seu nome: '), 
                  cpf=input('Digite seu Endereço:') , 
                  telefone=input('Digite seu Telefone: '))
    lista_de_pessoas.append(dados_cliente)

# Mostrando os Dados cliente.



os.system('cls')
print("\n = Exibindo Dados =")
for pessoa in lista_de_pessoas:
    pessoa.mostrar_dados()
print("\n = Somente Telefones = ")
for pessoa in lista_de_pessoas:
    pessoa.dados_sms_marketing()

