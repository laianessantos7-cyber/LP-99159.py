from dataclasses import dataclass
import os
os.system('cls')


@dataclass
class Endereco:
    logradouro: str
    numero: int
    estado: str
    cidade: str
@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: Endereco # Relacionamento com a classe Endereço. 

    def mostrar_dados(self):
        print(' = Mostrar dados das pessoas = ')
        print(f'Nome: {self.nome} \n' )
        print(f'E-mail:{self.email} \n')
        print('= ENDEREÇO = \n')
        print(f'Estado:{self.endereco.estado} \n')
        print(f'Cidade:{self.endereco.cidade} \n')
        print(f'Endereço: {self.endereco.logradouro} \n')
        print(f'Número: {self.endereco.numero} \n')


pessoa1=Pessoa(nome=input('Digite seu nome: \n'), 
               email=input('Digite seu E-mail: \n') ,
                 endereco=Endereco(
                     estado=input('Digite seu Estado: \n'),
                     cidade=input('Digite sua cidade: \n'), 
                     logradouro=input('Digite o logradouro: \n'),
                     numero=input('Digite o número do seu endereço: \n')))


# Mostrando os Dados cliente.
pessoa1.mostrar_dados()
