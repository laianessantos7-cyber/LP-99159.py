
import streamlit as st
import time

st.write("Laço de Repetição- FOR")

st.header("Escrever um algoritmo mostre os números ímpares entre 1 e 20.")

if st.button("Iniciar"):
    for i in range (1,21,2):
        st.info(i)
        time.sleep(0.5)
    st.header("FIM")

