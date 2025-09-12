import streamlit as st

st.title("Boletim Escolar: ")
st.write("Escrever um programa de computador que solicite do usuário 4 notas e, ao final, apresente a média: ")

soma=0
media=0
for i in range (4):
    nota=st.number_input(f"Digite a {i+1} º sua nota: " , max_value=10, min_value=0, step=1 )
    soma=soma+nota

media=soma/4

if st.button("Mostrar Resultado."):
        st.info(f"Média: {media}")
else:
      st.info("Coloque o número.")