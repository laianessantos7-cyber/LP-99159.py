#Verificando a média
#Solicite ao usuário a média do aluno
#Se maior ou igual a 7, mostre como aporvado
#Caso contrario, mostre reprovado

import streamlit as st

st.title("Verificando média")

media=st.number_input("Digite a média: ")

if st.button("Verificar"):
    if media >=7:
        st.write("Aprovado!")
    else: 
        st.write("Reprovado!")

else:
    st.info("Por favor, Digite sua média: ")


    #sucess- verde
    #warning- amarelo
    #info- azul
    #error- vermelho