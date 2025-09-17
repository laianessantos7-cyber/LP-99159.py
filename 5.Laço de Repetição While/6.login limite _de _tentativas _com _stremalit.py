import streamlit as st

st.title('Realize o seu login: ')

st.write("Crie um programa que solicite ao usuário seu login e uma senha.O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. O programa deve solicitar o login e senha apenas três vezes. Caso ultrapasse o número de tentativas, o programa deve ser finalizado.")

tentativas=4

email_salvo='laiane.s.santos@ba.estudante.senai.br'
senha_salva='123456'


email = st.text_input('Digite seu E-mail: ')
senha = st.text_input('Digite sua senha: ',type='password')


if st.button('Acessar'):
        if email==email_salvo and senha==senha_salva:
            st.success('Bem-vindo, login realizado com sucesso!')
    
else: 
        tentativas-=1
        if tentativas>0:
               st.error("Tentativa inválida! Restam {tentativas}.")
        else:
                st.error(' Você ultrapassou o número de tentativas, tente novamente mais tarde!')