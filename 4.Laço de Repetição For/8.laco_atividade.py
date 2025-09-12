
import streamlit as st
import time


st.title("Laço de Repeitição: For")

st.write("Escreva um algoritmo que mostra os números pares entre 100 e 120.")

if st.button("Iniciar"):
    for i in range (100,121,2):
        st.info(i)
        time.sleep(0.5)
    st.header("FIM")

