import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str

    def dados_entrega(self):
        print("\n = Dados de Entrega = ")
        print(f"Nome: {self.nome}")
        print(f'Endereço: {self.endereco}')
   
    def email_marketing(self):
        print("\n = Dados de E-mail Marketing = ")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")


print("Solicitando os dados da pessoa.")
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                 email=input('Digite seu E-mail: '),
                 endereco=input("Digite seu endereço: "))



print("\n = Exibindo Dados =")
pessoa1.dados_entrega()
pessoa1.email_marketing()