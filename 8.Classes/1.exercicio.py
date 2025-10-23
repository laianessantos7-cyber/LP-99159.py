from dataclasses import dataclass

@dataclass
class Informacoes_pessoa1:
    nome: str
    idade: int
    peso: float
    altura: float
   



print('Solicitando dados da pessoa')


pessoa1=Informacoes_pessoa1(nome=input('Digite seu nome: '),
                             idade=int(input('Digite sua idade: ')) , 
                             peso=float(input('Digite seu peso: ')),
                             altura= float(input('Digite sua altura:')), 
)

print('Exibindo dados das pessoa. ')
print(f'Nome:{pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}, Altura: {pessoa1.altura}') 


