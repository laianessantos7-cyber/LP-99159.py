import streamlit as st

st.title("Boletim Escolar: ")

soma=0


for i in range(2):
    n1=st.number_input(f"Digite a {i+1}º nota: ")
    if n1>=0 and n1<=10:
        break
   
media=n1+n1/2
soma=n1+n1
    
    
        

print(f"Nota: {media}")
print('FIM')