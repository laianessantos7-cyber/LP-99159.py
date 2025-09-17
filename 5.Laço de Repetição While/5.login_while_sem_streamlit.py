#Crie um programa que solicite ao usuário seu login e uma senha. 
#O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. 

import os
os.system('cls')
email_salvo='laiane.s.santos@ba.estudante.senai.br'
senha_salva='123456'


while True:
             email=input('Digite seu E-mail: ')
             senha=input('Digite sua senha: ')
             if email==email_salvo and senha==senha_salva:
                 print('Bem-vindo, login realizado com sucesso!')
                 break
             else:
                   print("Senha ou login inválidos.")
    