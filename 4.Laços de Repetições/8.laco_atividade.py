#Escreva um algoritmo que mostra os números pares entre 100 e 120.


import streamlit as st
import time


st.title("Atividade: 1")

st.header("Laço de repetições- FOR")

if st.button("Iniciar"):
    for i in range (100,121,2):
        st.info(i)
        time.sleep(0.5)
    st.sucess("FIM")

