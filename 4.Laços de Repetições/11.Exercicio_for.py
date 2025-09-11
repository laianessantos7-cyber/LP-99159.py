import streamlit as st
import time


st.title("Contagem Regressiva: ")
st.write("Escrever um algoritmo que solicite ao usuário um número e faça a contagem regressiva a partir do número informado até o número, aguardando um segundo para exibir cada número.")


numero = st.number_input("Informe um número: ",step=1)


if st.button("Contar"):
    for i in range(numero, 0,-1):
        st.write(i)
        time.sleep(1)
    st.snow()
    st.balloons( )
    st.header("FELIZ ANO NOVO!")