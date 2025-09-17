import streamlit as st

st.title('ÁREA DE LOGIN: ')

st.write('Crie um programa que solicite ao usuário seu login e uma senha. O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. ')

email_salvo='laiane.s.santos@ba.estudante.senai.br'
senha_salva='123456'

login=st.text_input('Digite seu E-mail: ')
senha=st.text_input('Digite sua senha: ' ,type='password')

if st.button('Acessar.'):
    if login==email_salvo and senha== senha_salva:
            st.write('Bem-vindo!')
    else:
        st.warning("Login ou senha inválidos!")