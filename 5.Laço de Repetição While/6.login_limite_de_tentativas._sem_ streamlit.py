#Crie um programa que solicite ao usuário seu login e uma senha. 
#O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. 
#O programa deve solicitar o login e senha apenas três vezes. Caso ultrapasse o número de tentativas, o programa deve ser finalizado.


import os
os.system('cls')


tentativas= 0
email_salvo='laiane.s.santos7@ba.estudante.senai.br'
senha_salvo='123456'

for i in range(3):
    while True:
        if tentativas>=3:
            break 
        print(f"\n Tentativa: {tentativas}")
        email = input('Digite seu E-mail: ')
        senha = input('Digite sua senha: ')


        if email==email_salvo and senha== senha_salvo:
            print('Bem-vindo, login realizado com sucesso!')
            break
        else: 
            print('Login ou senha inválidos.')
            tentativas+=1
    

        
       