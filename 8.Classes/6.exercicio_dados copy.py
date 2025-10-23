import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str

    def mostrar_dados(self):
        print("\n = Dados = ")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f'Endereço: {self.endereco}')
   
    def mostrar_somente_nome(self):
        print("\n = Somente nome = ")
        print(f"Nome: {self.nome}")
        


print("Solicitando os dados da primeira pessoa.")
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                 email=input('Digite seu E-mail: '),
                 endereco=input("Digite seu endereço: "))
print(' ')
print("Solicitando os dados da segunda pessoa.")
pessoa2 = Pessoa(nome=input("Digite seu nome: "),
                 email=input('Digite seu E-mail: '),
                 endereco=input("Digite seu endereço: "))


os.system('cls')
print("\n = Exibindo Dados =")
pessoa1.mostrar_dados()
pessoa1.mostrar_somente_nome()
pessoa2.mostrar_dados()
pessoa2.mostrar_somente_nome()