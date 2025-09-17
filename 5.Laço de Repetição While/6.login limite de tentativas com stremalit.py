


import streamlit as st

st.title(" Portal de Login")

st.write ("Crie um programa que solicite ao usuário seu login e uma senha.O programa deve continuar pedindo o login e a senha até que ambos estejam corretos. O programa deve solicitar o login e senha apenas três vezes. Caso ultrapasse o número de tentativas, o programa deve ser finalizado.")
email_correto = "laiane.s.santos@ba.estudante.senai.br"
senha_correta = "123456"


if "tentativas" not in st.session_state:
    st.session_state.tentativas = 3


if st.session_state.tentativas > 0:
    email = st.text_input("E-mail:")
    senha = st.text_input("Senha:", type="password")

    if st.button("Acessar"):
        if email == email_correto and senha == senha_correta:
            st.success(" Bem-vindo! Login realizado com sucesso.")
            st.session_state.tentativas = 0  
        else:
            st.session_state.tentativas -= 1
            if st.session_state.tentativas > 0:
                st.error(f" Login ou senha incorretos! Restam {st.session_state.tentativas} tentativas.")
            else:
                st.error("Você ultrapassou o número de tentativas. Tente novamente mais tarde!")
else:
    st.error(" Número de tentativas esgotado. Tente novamente mais tarde!")