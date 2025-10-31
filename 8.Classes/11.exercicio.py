
import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Livros:
    nome: str
    autor: str
    categoria: str
    preco: float

QUANTIDADE_ALUNOS= 3
lista_livro=[]

print('Solicitando dados do aluno')
for i in range(QUANTIDADE_ALUNOS):
    livro = Livros(
        nome=input('Nome: '),
        autor=input('Autor: '),
        categoria=input(('Categoria: ')),
        preco=(float(input('Preço: ')))
    )
    lista_livro.append(livro)

print()
print('Salvando dados')
catalogo='dados_livro.txt'

with open(catalogo, 'a') as catalogo_livro:
    for aluno in lista_livro:
        catalogo_livro.write(f'\n{livro.nome}, \n{livro.autor} , \n{livro.categoria}, \n{livro.preco}')
        print('Salvo com sucesso!')