from dataclasses import dataclass
import os
os.system('cls')


@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco # Relacionamento com a classe Endereço. 





pessoa1=Pessoa(nome='Laiane',
               idade=18 , 
               endereco=Endereco(logradouro='Rua B', 
               numero=25))

print(' = Mostrar dados das pessoas. =')
print(f'Nome: {pessoa1.nome}')
print(f'Idade: {pessoa1.idade}')
print(f'Endereço: {pessoa1.endereco.logradouro}')
print(f'Número: {pessoa1.endereco.numero}')