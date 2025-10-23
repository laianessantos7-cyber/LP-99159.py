import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str

    def mostrar_dados(self):
        print("\n = Todos os Dados = ")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f'Endereço: {self.endereco}')
   
    def mostrar_somente_nome(self):
        print(f"Nome: {self.nome}")
        


print("Solicitando os dados da pessoa.")
lista_pessoas=[]
for i in range (2):
    pessoa = Pessoa(nome=input("Digite seu nome: "),
                 email=input('Digite seu E-mail: '),
                 endereco=input("Digite seu endereço: "))
    lista_pessoas.append(pessoa)
print(' ')

os.system('cls')
print("\n = Exibindo Dados =")
for pessoa in lista_pessoas:
    pessoa.mostrar_dados()
print("\n = Somente nome = ")
for pessoa in lista_pessoas:
    pessoa.mostrar_somente_nome()
