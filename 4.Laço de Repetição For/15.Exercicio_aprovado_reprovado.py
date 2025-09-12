import streamlit as st

st.title("Verificando Média. ")
st.write("Escrever um programa de computador que solicite do usuário 3 notas e, ao final, apresente a média e mostre para o usuário se o aluno está aprovado, em recuperação ou reprovado. Considere que para aprovação, deve-se obter média maior ou igual a 7, para ser reprovado, a média deve ser menor que 4.")
soma=0
media=0
for i in range (3):
    nota=st.number_input(f"Digite a {i+1} º sua nota: " , max_value=10, min_value=0, step=1 )
    soma=soma+nota

media=soma/3

if st.button("Mostrar Resultado."):
        if media >=7:
            st.write("Aprovado!")
            st.info(f"Média: {media}")
            st.balloons()
        elif media >=4 and media <7:
              st.info("Recuperação")
              st.snow()
        elif media <4:
              st.info(f"Média{media}")
              st.error("Reprovado")

else:
      
      st.info("Coloque a nota.")