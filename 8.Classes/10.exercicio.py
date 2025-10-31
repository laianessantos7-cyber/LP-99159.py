from dataclasses import dataclass
import os
os.system('cls')


@dataclass # Criando Classe
class Autor:
    nome: str
    biografia: str
    
@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor


    def exibir_detalhes(self):
        print('===== Informaçãoes Do Livro =====')
        print(f'Titulo do Livro: {self.titulo} \n')
        print(f'Ano de Publicação: {self.ano} \n')
        print(f'Nome Do Autor: {self.autor.nome} \n')

livro_autor=Livro(titulo=input('Digite o Titulo Do Livro: '),
                 ano=int(input('Digite o ano de publicação do Livro:')),
                    autor=Autor(
                     nome=input('Digite o nome do Autor: '),
                        biografia=input('Digite a Biografia: ')))
                  

livro_autor.exibir_detalhes()
