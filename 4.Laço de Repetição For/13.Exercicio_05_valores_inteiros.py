import streamlit as st


st.title("Exercício, Contador de Números Pares e Ímpares: ")
st.write("Escreva um algoritmo que solicite ao usuário 5 valores inteiros e ao final mostre quantos números são pares " \
"quantos números são ímpares: ")



pares=0
impares=0





for i in range(1,6):
        numero=st.number_input(f"Digite o {i}º número", step=1)
        if numero % 2 == 0:
                pares = pares +  1
        else:
                impares = impares + 1

if st.button("Calcular."):  
    st.info(f"Quantos números são pares: {pares}")
    st.info(f"Quantos números são ímpares: {impares}")
    

    


    st.header("FIM")