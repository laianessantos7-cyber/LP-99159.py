from dataclasses import dataclass

@dataclass
class Informacoes_pessoa1:
    nome: str
    email:str
    telefone: str
    endereco: str
    



print('Solicitando dados da pessoa')


pessoa1=Informacoes_pessoa1(nome=input('Digite seu nome: '),
                             email=input(('Digite seu E-mai: ')) , 
                             telefone=float(input('Digite seu telefone: ')),
                             endereco= input('Digite seu Endereço:'), 
)


print('Exibindo dados das pessoa. ')
print(f'Nome:{pessoa1.nome}, E-mail: {pessoa1.email}, Telefone: {pessoa1.telefone}, Endereço: {pessoa1.endereco}') 


