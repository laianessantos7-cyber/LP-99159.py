import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float
    
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso}')
        print(f'Altura: {self.altura}')
   
    def envelhecer(self,anos):
        self.idade += anos
   
   
    def emagrecer(self,peso):
        self.peso -= peso
        
    def engordar(self,peso):
        self.peso += peso
        
        
        
print('Solicitando dados da pessoa.')


lista_pessoas=[]

pessoa1 = Pessoa (nome=input("Digite seu Nome: "),
                 idade=int(input('Digite sua Idade: ')),
                 peso=float(input("Digite seu Peso: ")),
                altura=float(input("Digite sua Altura: ")))
lista_pessoas.append(pessoa1)
print(' ')

pessoa1.mostrar_dados()
print("\nAtualizando dados...")
pessoa1.envelhecer(2)      # envelhece 2 anos
pessoa1.engordar(3)        # engorda 3 kg
pessoa1.emagrecer(1.5)     # emagrece 1.5 kg
pessoa1.mostrar_dados()    # mostra tudo atualizado




