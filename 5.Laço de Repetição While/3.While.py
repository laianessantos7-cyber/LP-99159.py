import streamlit as st

st.title("Laço de repetição- While.")

nota= st.number_input("Digite um número: ", step=1)

if st.button("Verificar"):
    if nota <0 or nota >10:
        st.warning("A nota deve ser entre 0 e 10.")

else:
    st.info(f"Nota: {nota}")