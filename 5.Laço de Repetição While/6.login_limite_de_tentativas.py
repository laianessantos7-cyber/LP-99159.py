#Crie um programa que solicite ao usuário seu login e uma senha. 
#O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. 
#O programa deve solicitar o login e senha apenas três vezes. Caso ultrapasse o número de tentativas, o programa deve ser finalizado.


import os
os.system('cls')

while True:
        tentativas=3
        while tentativas>3:
             email=input('Digite seu E-mail: ')
             senha=input('Digite sua senha: ')
             if email=='laiane.s.santos@ba.estudante.senai.br'and senha=='123456':
                 print('Bem-vindo, login realizado com sucesso!')
             break