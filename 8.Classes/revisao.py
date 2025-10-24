import os
os.system("cls")

from dataclasses import dataclass


# Criando uma classe.
# CPF? Endereço? Nome? Titulo do eleitor? E-mail? Telefone? 
# Seu sistema precisa de algumas informaçoes.
# Uma venda.
# Endereço, nome , telefone. (Mini-Mundo)


@dataclass
class Cliente:
    nome: str
    endereco: str
    telefone: str


# Funcão apenas desta classe.

    def mostrar_dados_cliente(self):
        print(f'Nome: {self.nome}')
        print(f'Endereço: {self.endereco}')
        print(f'Telefone: {self.telefone}')


# Criando dois clientes com as caracterisiticas definidas na classe.

lista_de_clientes=[]

for i in range(3):
    dados_cliente= Cliente(nome=input('Digite seu nome: '), 
                  endereco=input('Digite seu Endereço:') , 
                  telefone=input('Digite seu Telefone: '))
    lista_de_clientes.append(dados_cliente)

# Mostrando os Dados cliente.

for cliente in lista_de_clientes:
    cliente.mostrar_dados_cliente()
# Posição: 0, 1, 2

