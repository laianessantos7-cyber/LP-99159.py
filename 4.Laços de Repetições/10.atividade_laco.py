import streamlit as st
import time


st.title("Laço de Repetição- FOR")

st.write("Escreva um algoritmo que solicite do usuário um número e mostre a tabuada de multiplição do número informado: ")

n1=st.number_input("Informe o número: ")




if st.button("Calcular."):
    for i in range(11):
        time.sleep(0.5)
        n=n1*i
       
       
        st.info(f"{n1} x {i} = {n}")

st.header("FIM")

