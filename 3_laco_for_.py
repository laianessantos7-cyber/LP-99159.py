import streamlit as st

st.title("Contagem regressiva")

for i in range(10,-1,-1):
    st.write(i)


st.write("FELIZ ANO NOVO!")