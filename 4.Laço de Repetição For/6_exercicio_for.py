import streamlit as st

st.title("Verificando")

n1=st.number_input("Digite o primeiro numero: ", min_value=0 , max_value=100)
print("")
n2=st.number_input("Digite o segundo numero: ",min_value=0,max_value=100)

soma= n1+n2
media= (n1+n2)/2
produto=n1*n2
print("")
maior=max(n1, n2)
menor=min(n1, n2)


if st.button("Verificar."):
    if n1 and n2:
      st.write(f"Soma: {soma}") 
      st.write(f"Produto: {produto}")  
      st.write(f"Maior: {maior}")
      st.write(f"Menor: {menor}")
      st.write(f"Média: {media}")

else:
    st.info("Informe os números: ")
