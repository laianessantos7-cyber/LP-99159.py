
#Escrever um algoritmo mostre os números ímpares entre 1 e 20.
import streamlit as st
import time

st.title("Atividade: 2")

st.header("Laço de Repetição- FOR")

if st.button("Iniciar"):
    for i in range (1,20,2):
        st.info(i)
        time.sleep(0.5)
    st.header("FIM")

