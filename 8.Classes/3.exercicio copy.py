from dataclasses import dataclass

@dataclass
class Informacoes_pessoa1:
    nome: str
    email:str
    telefone: str
    endereco: str
    
    def mostrar_dados(self):
            print(f'Nome:{self.nome})') 
            print(f'E-mail: {self.email}')
            print(f'Telefone: {self.telefone}')
            print(f'Endereço: {self.endereco}')

print('Solicitando dados da pessoa')


pessoa1=Informacoes_pessoa1(nome=input('Digite seu nome: '),
                             email=input(('Digite seu E-mai: ')) , 
                             telefone=float(input('Digite seu telefone: ')),
                             endereco= input('Digite seu Endereço:'), 
)





