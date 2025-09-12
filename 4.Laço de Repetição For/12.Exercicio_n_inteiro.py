import streamlit as st
import time

st.title("Exercício: ")
st.write("Escrever um programa de computador que solicite do usuário 5 números inteiros e, ao final, apresente a soma de todos os números lidos.")



n1=st.number_input("Digite o primeiro número: ", step=1)
n2=st.number_input("Digite o segundo número: ", step=1)
n3=st.number_input("Digite o terceiro número: ", step=1)
n4=st.number_input("Digite o quarto número: " , step=1)
n5=st.number_input("Digite o quinto número: ", step=1)
soma=n1+n2+n3+n4+n5

if st.button("Calcular."):
    for i in range(5):
        time.sleep(0.5)

st.write(f"Resultado:  {soma}")