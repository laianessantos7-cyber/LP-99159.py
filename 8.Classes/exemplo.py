# EXEMPLO: 

from dataclasses import dataclass
# Estrutura de dados : classe.
@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

# Exemplo de uso da classe
pessoa1= Pessoa('Laiane' , 18 , 86568745625)
pet1 = Pet('Flocos' , 1 , 5)

print('Exibindo dados da Pessoa.')
print(f'Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, CPF: {pessoa1.cpf}')
print('')
print('Exibindo dados do Pet')
print(f'Nome: {pet1.nome}, Idade: {pet1.idade}, Peso: {pet1.peso}')