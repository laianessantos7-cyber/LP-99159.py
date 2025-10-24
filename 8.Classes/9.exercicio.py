from dataclasses import dataclass
import os
os.system('cls')


@dataclass # Criando Classe
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostrar_dados(self):
        print(' = Mostrar dados das pessoas = ')
        print(f'Nome: {self.nome} \n' )
        print(f'Idade:{self.idade} \n')
        print(f'Peso:{self.peso} \n')
        print(f'Altura:{self.altura} \n')
        

print("Solicitando os dados.")
lista_pessoas=[]

for i in range (4):
    print(f"\n--- Pessoa {i + 1} ---")
    pessoa = Pessoa(nome=input("Digite seu Nome: "),
                 idade=input('Digite sua Idade: '),
                 peso=input("Digite seu Peso: "),
                altura=input("Digite sua Altura: "))
    lista_pessoas.append(pessoa)
print(' ')

os.system('cls')
# Mostrando os Dados Pessoa.

for pessoa in lista_pessoas:
    pessoa.mostrar_dados()

